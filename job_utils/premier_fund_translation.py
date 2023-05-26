
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    premier_fund_translation_df = spark.sql("SELECT voya_fund_number, premier_fund_number, voya_fund_name,to_date(created_timestamp) as created_timestamp, created_by, source_file_name, as_of_date as source_cycle_date, process_control_id,'IMPALA' as source_system from premier_fund_translation_csv")

    transform_df = premier_fund_translation_df

    return transform_df