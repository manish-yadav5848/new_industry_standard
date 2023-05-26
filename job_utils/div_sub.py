
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    exn_xxewre01_xxewrdpg_jb_df = spark.sql("SELECT client_id,plan_number,div_sub_id,cast(null as varchar(36)) as div_sub_key,address_city,address_line_1,address_line_2,address_line_3,address_state,address_zip_code,primary_name,secondary_name,'VRP-PB' as source_system,source_cycle_date FROM exn_xxewre01_xxewrdpg_jb")

    super_omni_newr_plan_divsub_daily_ng_dat_df = spark.sql("SELECT client_id,plan_number,div_sub_id,cast(null as varchar(36)) as div_sub_key,address_city,address_line_1,address_line_2,address_line_3,address_state,address_zip_code,primary_name,secondary_name,'VRP-SP' as source_system,source_cycle_date FROM super_omni_newr_plan_divsub_daily_ng_dat")

    transform_df = exn_xxewre01_xxewrdpg_jb_df.unionByName(super_omni_newr_plan_divsub_daily_ng_dat_df)

    return transform_df