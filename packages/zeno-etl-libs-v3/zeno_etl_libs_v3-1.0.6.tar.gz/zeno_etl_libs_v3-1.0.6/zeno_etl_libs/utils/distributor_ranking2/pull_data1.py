Q_SB = """
    select sb.id as "sb-id", sb."store-id" , sb."drug-id" , 
        sb.quantity as "sb-quantity", sbol."ordered-dist-id" , 
        sbol."required-quantity" , sbol.status , sbol."ff-status" , 
        date(sb."created-at") as "sb-created-on", 
        sbol."created-at" as "sbol-created-at" 
    from 
        "{schema}"."short-book-1" sb 
    left join 
        "{schema}"."short-book-order-logs" sbol 
        on sbol."short-book-id" = sb.id 
    where 
        sb."distributor-id" not in (8105, 5000, 76) 
        and DATEDIFF(day, date(sb."created-at"), '{reset_date}') <= {time_interval} 
        and DATEDIFF(day, date(sb."created-at"), '{reset_date}') >= 7
        and sbol.status not in ('presaved', 'saved')
        {franchisee_stores_execute_query}
    order by 
        sb.id, sbol."created-at" 
    """
# (2,4,7,16,54,82,231,234,244,278,297,23,28,39,216,218,235,229,280,8,13,21,26,31,45,188,208,221,222,230,241,260,264,20,36,61,134,160,184,195,215,224,226,245,252,273,281)
Q_RATES = """
    select subQ."distributor-id", subQ."drug-id", avg(subQ.mrp) as avg_mrp, 
        avg(subQ."purchase-rate") as avg_purchase_rate
    from 
        (
        select i."distributor-id" , ii."drug-id" , i."created-at" , inv.mrp ,
            inv."purchase-rate", row_number() over (partition by 
                i."distributor-id", ii."drug-id"  
                order by i."created-at" desc) as recency_rank
        from 
            "{schema}".invoices i 
        left join 
            "{schema}"."invoice-items-1" ii 
            on ii."invoice-id" = i.id
        left join 
            "{schema}"."inventory-1" inv 
            on inv."invoice-item-id" = ii.id 
        where 
            DATEDIFF(day, date(i."created-at"), '{reset_date}') <= {time_interval} 
            and DATEDIFF(day, date(i."created-at"), '{reset_date}') >= 7
            and i."distributor-id" not in (8105, 76, 5000) 
        ) as subQ 
    where 
        subQ.recency_rank <= 5 
    group by subQ."distributor-id", subQ."drug-id" 
    """

Q_STORE_DC_MAPS = """
    select subQ.*, s2."name" as "dc-name"
    from
        (
        select sdm."store-id" , s."name" as "store-name", 
            "forward-dc-id" as "dc-id"
        from 
            "{schema}"."store-dc-mapping" sdm 
        left join 
            "{schema}".stores s on sdm."store-id" = s.id 
        where "forward-dc-id" not in (199)
        group by "store-id" , s."name", "forward-dc-id" 
        ) as subQ
    left join "{schema}".stores s2 
        on subQ."dc-id" = s2.id
    """

Q_DRUGS = """
    select id as "drug-id", "drug-name" , "type" as "drug-type"
    from "{schema}".drugs d 
    """

Q_DISTRIBUTORS = """
    select db.id as "distributor-id", db.name as "distributor-name", 
        db."credit-period" as "distributor-credit-period", 
        d."type" as "drug-type", count(distinct dd."drug-id") as "dist-type-portfolio-size"
    from 
        "{schema}".distributors db
    left join 
        "{schema}"."distributor-drugs" dd on db.id = dd."distributor-id" 
    left join 
        "{schema}".drugs d on dd."drug-id" = d.id 
    group by db.id, "distributor-name", "distributor-credit-period", "drug-type"
    """

Q_DC_DISTRIBUTOR_MAPPING = """
    select "dc-id", "distributor-id"
    from "{schema}"."dc-distributor-mapping" ddm 
    where "is-active" = 1
    group by "dc-id" , "distributor-id"
    """

Q_DISTRIBUTOR_DRUGS = """
    select "distributor-id", "drug-id" 
    from "{schema}"."distributor-drugs" dd 
    group by "distributor-id" , "drug-id"
    """

Q_FRANCHISEE_STORES = """
    select distinct "id"
    from "{schema}".stores
    where name <> 'Zippin Central'
    and "is-active" = 1
    and "opened-at" != '0101-01-01 00:00:00'
    and "franchisee-id" != 1 
    """


def pull_data_dc(reset_date, time_interval, db, schema):
    df_sb = db.get_df(Q_SB.format(
        reset_date=reset_date, time_interval=time_interval, schema=schema,
        franchisee_stores_execute_query=""))
    df_sb.columns = [c.replace('-', '_') for c in df_sb.columns]

    df_rates = db.get_df(Q_RATES.format(
        reset_date=reset_date, time_interval=time_interval, schema=schema))
    df_rates.columns = [c.replace('-', '_') for c in df_rates.columns]

    df_store_dc_maps = db.get_df(Q_STORE_DC_MAPS.format(schema=schema))
    df_store_dc_maps.columns = [c.replace('-', '_') for c in
                                df_store_dc_maps.columns]

    df_drugs = db.get_df(Q_DRUGS.format(schema=schema))
    df_drugs.columns = [c.replace('-', '_') for c in df_drugs.columns]

    df_distributors = db.get_df(Q_DISTRIBUTORS.format(schema=schema))
    df_distributors.columns = [c.replace('-', '_') for c in
                               df_distributors.columns]
    df_distributors = df_distributors.dropna()
    df_distributors = df_distributors.loc[df_distributors["drug_type"] != '']

    df_dc_distributors_mapping = db.get_df(
        Q_DC_DISTRIBUTOR_MAPPING.format(schema=schema))
    df_dc_distributors_mapping.columns = [c.replace('-', '_') for c in
                                          df_dc_distributors_mapping.columns]

    df_distributor_drugs = db.get_df(Q_DISTRIBUTOR_DRUGS.format(schema=schema))
    df_distributor_drugs.columns = [c.replace('-', '_') for c in
                                    df_distributor_drugs.columns]
    df_distributor_drugs.drop_duplicates(inplace=True)

    # ensure data types
    df_rates["avg_mrp"] = df_rates["avg_mrp"].astype(float)
    df_rates["avg_purchase_rate"] = df_rates["avg_purchase_rate"].astype(float)

    return df_sb, df_rates, df_store_dc_maps, df_drugs, df_distributors, \
           df_dc_distributors_mapping, df_distributor_drugs


def pull_data_franchisee(reset_date, franchisee_stores, time_interval,
                         db, schema):
    df_franchisee_stores = db.get_df(Q_FRANCHISEE_STORES.format(schema=schema))
    all_franchisee_stores = df_franchisee_stores["id"].to_list()

    if franchisee_stores == [0]:
        franchisee_stores_execute_query = f"""
        and sb."store-id" in {str(all_franchisee_stores).replace('[', '(').replace(']', ')')}
        """
    else:
        # only take valid franchisee stores
        franchisee_stores = list(
            set(franchisee_stores).intersection(all_franchisee_stores))

        franchisee_stores_execute_query = f"""
        and sb."store-id" in {str(franchisee_stores).replace('[', '(').replace(']', ')')}
        """

    df_sb = db.get_df(Q_SB.format(
        reset_date=reset_date, time_interval=time_interval, schema=schema,
        franchisee_stores_execute_query=franchisee_stores_execute_query))
    df_sb.columns = [c.replace('-', '_') for c in df_sb.columns]

    df_rates = db.get_df(Q_RATES.format(
        reset_date=reset_date, time_interval=time_interval, schema=schema))
    df_rates.columns = [c.replace('-', '_') for c in df_rates.columns]

    df_store_dc_maps = db.get_df(Q_STORE_DC_MAPS.format(schema=schema))
    df_store_dc_maps.columns = [c.replace('-', '_') for c in
                                df_store_dc_maps.columns]

    df_drugs = db.get_df(Q_DRUGS.format(schema=schema))
    df_drugs.columns = [c.replace('-', '_') for c in df_drugs.columns]

    df_distributors = db.get_df(Q_DISTRIBUTORS.format(schema=schema))
    df_distributors.columns = [c.replace('-', '_') for c in
                               df_distributors.columns]
    df_distributors = df_distributors.dropna()
    df_distributors = df_distributors.loc[df_distributors["drug_type"] != '']

    df_dc_distributors_mapping = db.get_df(
        Q_DC_DISTRIBUTOR_MAPPING.format(schema=schema))
    df_dc_distributors_mapping.columns = [c.replace('-', '_') for c in
                                          df_dc_distributors_mapping.columns]

    df_distributor_drugs = db.get_df(Q_DISTRIBUTOR_DRUGS.format(schema=schema))
    df_distributor_drugs.columns = [c.replace('-', '_') for c in
                                    df_distributor_drugs.columns]
    df_distributor_drugs.drop_duplicates(inplace=True)

    # ensure data types
    df_rates["avg_mrp"] = df_rates["avg_mrp"].astype(float)
    df_rates["avg_purchase_rate"] = df_rates["avg_purchase_rate"].astype(float)

    return df_sb, df_rates, df_store_dc_maps, df_drugs, df_distributors, \
           df_dc_distributors_mapping, df_distributor_drugs
