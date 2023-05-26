
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    auto_method_df = spark.sql("SELECT plan_number, company_code, tin, cast(payment_group as DECIMAL(19,0)) as payment_group , automation_method, created_timestamp, created_by, source_file_name, as_of_date as source_cycle_date, process_control_id,'IMPALA' as source_system from pdab_auto_method_csv")

    transform_df = auto_method_df

    return transform_df