"""
To save the cost, staging servers are switched off at 8PM IST and switched on at 9AM IST,
so we need to start and stop the DMS accordingly. This script will help us schedule the same.
"""
import argparse
import os
import sys

sys.path.append('../../../..')

from zeno_etl_libs.logger import get_logger
from zeno_etl_libs.helper.aws.dms import DMS

parser = argparse.ArgumentParser(description="This is ETL script.")
parser.add_argument('-e', '--env', default="dev", type=str, required=False,
                    help="This is env(dev, stage, prod)")
parser.add_argument('-ids', '--task_ids', default="CBS5J6V4AVST5D3DEZSQDNH363A37XI4F6JU3II",
                    type=str, required=False,
                    help="task id in csv")
args, unknown = parser.parse_known_args()
env = args.env
task_ids = args.task_ids

os.environ['env'] = env
logger = get_logger()

logger.info(f"env: {env}")

""" DMS class """
dms = DMS()

for task_id in task_ids.split(','):
    logger.info(f"task id: {task_id}")
    response = dms.stop(task_id=task_id)

    logger.info(f"response: {response}")
