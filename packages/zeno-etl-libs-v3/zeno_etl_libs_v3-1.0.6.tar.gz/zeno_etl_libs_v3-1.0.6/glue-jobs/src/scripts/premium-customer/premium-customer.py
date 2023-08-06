"""
# Author - shubham.gupta@zeno.health
# Purpose - script with DSS write action for premium customer
"""

import argparse
import os
import sys
from datetime import datetime as dt

import pandas as pd
from dateutil.tz import gettz

sys.path.append('../../../..')

from zeno_etl_libs.helper.aws.s3 import S3
from zeno_etl_libs.db.db import DB
from zeno_etl_libs.helper import helper
from zeno_etl_libs.logger import get_logger
from zeno_etl_libs.helper.email.email import Email
from zeno_etl_libs.helper.parameter.job_parameter import parameter

parser = argparse.ArgumentParser(description="This is ETL script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False)

args, unknown = parser.parse_known_args()
env = args.env
os.environ['env'] = env
job_params = parameter.get_params(job_id=42)
email_to = job_params['email_to']

logger = get_logger()

# params
# Segment calculation date should be 1st of every month

try:
    period_end_d_plus1 = job_params['period_end_d_plus1']
    period_end_d_plus1 = str(dt.strptime(period_end_d_plus1, "%Y-%m-%d").date())
    period_end_d_plus1 = period_end_d_plus1[:-3] + '-01'
except ValueError:
    period_end_d_plus1 = dt.today().strftime('%Y-%m') + '-01'

logger.info(f"segment calculation date : {period_end_d_plus1}")

read_schema = 'prod2-generico'
table_name = 'premium-segment'

rs_db = DB()
rs_db.open_connection()

s3 = S3()

table_info = helper.get_table_info(db=rs_db, table_name=table_name, schema=read_schema)
logger.info(table_info)
if isinstance(table_info, type(None)):
    logger.info(f"table: {table_name} do not exist")

p1_q = f"""
        select
            t.*,
            pm."primary-store-id",
            3 as "sort-seq"
        from
            (
            select
                "patient-id",
                '3m consecutive' "type",
                sum("total-spend") as "3m-total-spend",
                count(distinct rm.id) as "3m-nob",
                avg(case when "ecom-flag"=true then 1.00 else 0.00 end) as "ecom-perc"
            from
                "prod2-generico"."retention-master" rm
            where
                "created-at" between dateadd('month',
                -3,
                date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
            group by
                "patient-id"
            having
                count(distinct "bill-month") = 3
                and avg("total-spend")>=250) t
                left join (
                        select
                            ps."patient-id",
                            ps."store-id" as "primary-store-id"
                        from
                            (
                            select
                                rm."patient-id",
                                rm."store-id" ,
                                count(distinct rm.id) "nob",
                                max(rm."created-at") "recent_bill",
                                rank() over (partition by rm."patient-id"
                            order by
                                "nob" desc,
                                "recent_bill" desc) as rank
                            from
                                "prod2-generico"."retention-master" rm
                            where
                                rm."created-at" between dateadd('month',
                                -3,
                                date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
                            group by
                                rm."patient-id",
                                rm."store-id") ps
                        where
                            ps."rank" = 1 
                    ) pm on
            t."patient-id" = pm."patient-id";
        """
logger.info(f"data query : {p1_q}")
data_1 = rs_db.get_df(query=p1_q)

p2_q = f"""
        select
            x1."patient-id",
            'top-total-spend' as "type",
            x1."primary-store-id",
            1 as "sort-seq",
            "total-sales" as "3m-total-spend",
            "3m-nob",
            "ecom-perc"
        from
            (
            select
                rm."patient-id",
                pm."primary-store-id",
                count(distinct rm.id) as "3m-nob",
                sum(rm."total-spend") "total-sales",
                avg(case when "ecom-flag"=true then 1.00 else 0.00 end) as "ecom-perc",
                percent_rank() over ( partition by pm."primary-store-id" order by "total-sales" desc) "rank-total-revenue"            
            from
                "prod2-generico"."retention-master" rm
            left join (
                    select
                        ps."patient-id",
                        ps."store-id" as "primary-store-id"
                    from
                        (
                        select
                            rm."patient-id",
                            rm."store-id" ,
                            count(distinct rm.id) "nob",
                            max(rm."created-at") "recent_bill",
                            rank() over (partition by rm."patient-id"
                        order by
                            "nob" desc,
                            "recent_bill" desc) as rank
                        from
                             "prod2-generico"."retention-master" rm
                        where
                            rm."created-at" between dateadd('month',
                            -3,
                            date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
                        group by
                            rm."patient-id",
                            rm."store-id") ps
                    where
                        ps."rank" = 1 ) pm on
                pm."patient-id" = rm."patient-id"
            where
                rm."created-at" between dateadd('month',
                -3,
                date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
            group by
                rm."patient-id",
                pm."primary-store-id"
            ) x1
        where
            (x1."rank-total-revenue" <= 0.05)
        """
logger.info(f"data query : {p2_q}")
data_2 = rs_db.get_df(query=p2_q)

p3_q = f"""
        select
            x1."patient-id",
            'top-generic-spend' "type",
            x1."primary-store-id",
            2 as "sort-seq",
            "total-sales" as "3m-total-spend",
            "3m-nob",
            "ecom-perc"
        from
            (
            select
                rm."patient-id",
                pm."primary-store-id",
                count(distinct id) as "3m-nob",
                sum("spend-generic") "total-generic-sales",
                avg(case when "ecom-flag"=true then 1.00 else 0.00 end) as "ecom-perc",
                sum("total-spend") "total-sales",
                percent_rank() over (partition by pm."primary-store-id"
            order by
                "total-generic-sales" desc) "rank-generic-revenue"
            from
                "prod2-generico"."retention-master" rm
            left join (
            select
                ps."patient-id",
                ps."store-id" as "primary-store-id"
            from
                (
                select
                    rm."patient-id",
                    rm."store-id",
                    count(distinct rm.id) "nob",
                    max(rm."created-at") "recent_bill",
                    rank() over (partition by rm."patient-id"
                order by
                    "nob" desc,
                    "recent_bill" desc) as rank
                from
                     "prod2-generico"."retention-master" rm
                where
                    rm."created-at" between dateadd('month',
                    -3,
                    date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
                group by
                    rm."patient-id",
                    rm."store-id") ps
            where
                ps."rank" = 1 ) pm on
        pm."patient-id" = rm."patient-id"
            where
                rm."created-at" between dateadd('month',
                -3,
                date_trunc('month', date('{period_end_d_plus1}'))) and date_trunc('month', date('{period_end_d_plus1}'))
            group by
                rm."patient-id",
                pm."primary-store-id"
            ) x1
                where
            (x1."rank-generic-revenue" <= 0.05)
        """
logger.info(f"data query : {p3_q}")
data_3 = rs_db.get_df(query=p3_q)

data = pd.concat([data_1, data_3, data_3])

data = data.sort_values('sort-seq', ascending=True).groupby('patient-id', as_index=False).first()

data['primary-store-id'] = data['primary-store-id'].fillna(0)
data['primary-store-id'] = data['primary-store-id'].astype(int)
data = data.sort_values('3m-total-spend', ascending=False)

# Splitting Ecomm and Store Premium Customers
# Based on : if 50% or more bills on ecomm then Ecomm users

data_ecomm = data[data["ecom-perc"] >= 0.5]
data_store = data[data["ecom-perc"] < 0.5]

data_store['assignment'] = 1
data_ecomm['assignment'] = 1

# Store assignment
data_store['assignment'] = data_store.groupby('primary-store-id', as_index=False)['assignment'].cumsum()
data_store['assign-pharmacist'] = data_store['assignment'] % 4 + 1  # Assigning in equal 4 parts

# Ecomm assignment
data_ecomm['primary-store-id'] = 0
data_ecomm['assignment'] = data_ecomm.groupby('primary-store-id', as_index=False)['assignment'].cumsum()
data_ecomm['assign-pharmacist'] = data_ecomm['assignment'] % 14 + 1  # Assigning in equal 14 parts

# Merging Data

data = pd.concat([data_store, data_ecomm])

data['segment-calc-date'] = period_end_d_plus1

# Write to csv
s3.save_df_to_s3(df=data,
                 file_name=f'Shubham_G/premium_customer/premium_customer_{period_end_d_plus1}.csv')

# etl
data['created-at'] = dt.now(tz=gettz('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
data['created-by'] = 'etl-automation'
data['updated-at'] = dt.now(tz=gettz('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
data['updated-by'] = 'etl-automation'

logger.info(f"data write : \n {data.head()}")

# truncate data if current month data already exist

if isinstance(table_info, type(None)):
    logger.info(f"table: {table_name} do not exist")
else:
    truncate_query = f"""
            DELETE
            FROM
                "{read_schema}"."{table_name}"
            WHERE
                "segment-calc-date" = '{period_end_d_plus1}';
                """
    logger.info(truncate_query)
    rs_db.execute(truncate_query)

# drop duplicates subset - patient-id
data.drop_duplicates(subset=['patient-id'], inplace=True)

# Write to db
s3.write_df_to_db(df=data[table_info['column_name']], table_name=table_name,
                  db=rs_db, schema=read_schema)

logger.info("Script ran successfully")

total_patients = data['patient-id'].nunique()

# email after job ran successfully
email = Email()

mail_body = f"premium customer upload succeeded for segment calculation date {period_end_d_plus1} " \
            f"with data shape {data.shape} and total patient count {total_patients}"

if data.shape[0] == total_patients:
    subject = "Task Status segment calculation : successful"
else:
    subject = "Task Status segment calculation : failed"

email.send_email_file(subject=subject,
                      mail_body=mail_body,
                      to_emails=email_to, file_uris=[], file_paths=[])

# closing connection
rs_db.close_connection()
