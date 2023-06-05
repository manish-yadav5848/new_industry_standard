
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from wealthcentral.jobs.raw_to_transform.helper_utils.data_utils import merge_dataframes


def transform(spark: SparkSession, primary_key: list):

    super_omni_newr_partacctms_daily_ng_dat_df = spark.sql("select client_id, plan_number, participant_id, money_source_code as money_source, cast(null as DECIMAL(13,2)) as actual_contribution_amount, cast(null as DECIMAL(13,2)) as actual_contribution_percent, cast(null as DECIMAL(11,2)) as catchup_future_deferral_amount, cast(null as DECIMAL(11,2)) as deferral_dollar_amount_elected, cast(NULL  as VARCHAR(1)) as deferral_selection, cast(null as DECIMAL(9,6)) as ee_catchup_deferral_percent, cast(null as DECIMAL(9,6)) as ee_deferral_rate_elect, cast(null as DECIMAL(13,2)) as elected_contribution_amount, cast(null as DECIMAL(13,2)) as elected_contribution_percent, cast(null as DATE) as rate_escalator_creation_date, cast(null as DECIMAL(7,2)) as rate_escalator_dollar_amount, cast(null as DATE) as first_contribution_date, cast(null as DATE) as first_roth_contribution_date, cast(null as DECIMAL(9,6)) as future_catchup_def_pct, cast(null as DATE) as next_scheduled_increase_date, cast(null as DECIMAL(9,6)) as one_time_deferral_percent, cast(null as DECIMAL(13,2)) as prior_deferral_amount, cast(null as DECIMAL(13,2)) as prior_deferral_rate, cast(null as VARCHAR(1)) as rate_escalator_frequency, cast(null as DECIMAL(7,2)) as rate_escalator_inc_percent, cast(null as DECIMAL(7,2)) as rate_escalator_max_percent, cast(null as DECIMAL(6,3)) as source_adj_vest_percent, cast(null as DECIMAL(13,2)) as supplemental_deferral_dollar_prior, 'VRP-PB' as source_system, cast(source_cycle_date as DATE) as source_cycle_date,cast(null as DATE) as source_processing_date, cast(null as DECIMAL(11,2)) as actual_deferral_amount,deferral_rate_actual as deferral_rate_actual, cast(null as DECIMAL(11,2)) as catchup_deferral_amount, money_source_name from super_omni_newr_partacctms_daily_ng_dat")

    super_omni_newr_partacctms_daily_jb_dat_df = spark.sql("select client_id, plan_number, participant_id, money_source_code as money_source, cast(null as DECIMAL(13,2)) as actual_contribution_amount, cast(null as DECIMAL(13,2)) as actual_contribution_percent, cast(null as DECIMAL(11,2)) as catchup_future_deferral_amount, cast(null as DECIMAL(11,2)) as deferral_dollar_amount_elected, cast(NULL  as VARCHAR(1)) as deferral_selection, cast(null as DECIMAL(9,6)) as ee_catchup_deferral_percent, cast(null as DECIMAL(9,6)) as ee_deferral_rate_elect, cast(null as DECIMAL(13,2)) as elected_contribution_amount, cast(null as DECIMAL(13,2)) as elected_contribution_percent, cast(null as DATE) as rate_escalator_creation_date, cast(null as DECIMAL(7,2)) as rate_escalator_dollar_amount, cast(null as DATE) as first_contribution_date, cast(null as DATE) as first_roth_contribution_date, cast(null as DECIMAL(9,6)) as future_catchup_def_pct, cast(null as DATE) as next_scheduled_increase_date, cast(null as DECIMAL(9,6)) as one_time_deferral_percent, cast(null as DECIMAL(13,2)) as prior_deferral_amount, cast(null as DECIMAL(13,2)) as prior_deferral_rate, cast(null as VARCHAR(1)) as rate_escalator_frequency, cast(null as DECIMAL(7,2)) as rate_escalator_inc_percent, cast(null as DECIMAL(7,2)) as rate_escalator_max_percent, cast(null as DECIMAL(6,3)) as source_adj_vest_percent, cast(null as DECIMAL(13,2)) as supplemental_deferral_dollar_prior, 'VRP-SP' as source_system, cast(source_cycle_date as DATE) as source_cycle_date,cast(null as DATE) as source_processing_date, cast(null as DECIMAL(11,2)) as actual_deferral_amount, deferral_rate_actual as deferral_rate_actual, cast(null as DECIMAL(11,2)) as catchup_deferral_amount, money_source_name from super_omni_newr_partacctms_daily_jb_dat")

    exn_xxewre01_xxewrpps_ng_df = spark.sql("select client_id, plan_number, participant_id, money_source, cast(actual_contribution_amount as DECIMAL(13,2)) as actual_contribution_amount, cast(actual_contribution_percent as DECIMAL(13,2)) as actual_contribution_percent, cast(catch_up_future_deferral_amount as DECIMAL(11,2)) as catchup_future_deferral_amount, cast(deferral_dollar_amount_elected as DECIMAL(11,2)) as deferral_dollar_amount_elected, deferral_selection, cast(ee_catch_up_deferral_percent as DECIMAL(9,6)) as ee_catchup_deferral_percent, cast(ee_source_level_deferral_rate_elected as DECIMAL(9,6)) as ee_deferral_rate_elect, cast(elected_contribution_amount as DECIMAL(13,2)) as elected_contribution_amount,cast(elected_contribution_percent as DECIMAL(13,2)) as elected_contribution_percent, cast(escalator_creation_date as DATE) as rate_escalator_creation_date, cast(escalator_dollar_amount as DECIMAL(7,2)) as rate_escalator_dollar_amount, cast(first_contribution_date as DATE) as first_contribution_date, cast(first_roth_contribution_date as DATE) first_roth_contribution_date, cast(future_catchup_deferral as DECIMAL(9,6)) as future_catchup_def_pct, cast(next_scheduled_increase_date as DATE) as next_scheduled_increase_date, cast(one_time_deferral_percent as DECIMAL(9,6)) as one_time_deferral_percent, cast(prior_def_amount as DECIMAL(13,2)) as prior_deferral_amount, cast(prior_def_rate as DECIMAL(13,2)) as prior_deferral_rate, rate_escalator_frequency, cast(rate_escalator_inc_percent as DECIMAL(7,2)) as rate_escalator_inc_percent, cast(rate_escalator_max_percent as DECIMAL(7,2)) as rate_escalator_max_percent, cast(source_adj_vest_percent as DECIMAL(6,3)) as source_adj_vest_percent, cast(supplemental_def_dollar_prior as DECIMAL(13,2)) as supplemental_deferral_dollar_prior, 'VRP-PB' as source_system, cast(source_cycle_date as DATE) as source_cycle_date,cast(null as DATE) as source_processing_date, cast(actual_deferral_amount as DECIMAL(11,2)) as actual_deferral_amount, cast(null as varchar(20)) as deferral_rate_actual, cast(catch_up_deferral_amount as DECIMAL(11,2)) as catchup_deferral_amount, cast(null as VARCHAR(30)) as money_source_name from exn_xxewre01_xxewrpps_ng")

    exn_xxewre01_xxewrpps_jb_df = spark.sql("select client_id, plan_number, participant_id, money_source, cast(actual_contribution_amount as DECIMAL(13,2)) as actual_contribution_amount, cast(actual_contribution_percent as DECIMAL(13,2)) as actual_contribution_percent, cast(catch_up_future_deferral_amount as DECIMAL(11,2)) as catchup_future_deferral_amount, cast(deferral_dollar_amount_elected as DECIMAL(11,2)) as deferral_dollar_amount_elected, deferral_selection, cast(ee_catch_up_deferral_percent as DECIMAL(9,6)) as ee_catchup_deferral_percent, cast(ee_source_level_deferral_rate_elected as DECIMAL(9,6)) as ee_deferral_rate_elect, cast(elected_contribution_amount as DECIMAL(13,2)) as elected_contribution_amount,cast(elected_contribution_percent as DECIMAL(13,2)) as elected_contribution_percent, cast(escalator_creation_date as DATE) as rate_escalator_creation_date, cast(escalator_dollar_amount as DECIMAL(7,2)) as rate_escalator_dollar_amount, cast(first_contribution_date as DATE) as first_contribution_date, cast(first_roth_contribution_date as DATE) first_roth_contribution_date, cast(future_catchup_deferral as DECIMAL(9,6)) as future_catchup_def_pct, cast(next_scheduled_increase_date as DATE) as next_scheduled_increase_date, cast(one_time_deferral_percent as DECIMAL(9,6)) as one_time_deferral_percent, cast(prior_def_amount as DECIMAL(13,2)) as prior_deferral_amount, cast(prior_def_rate as DECIMAL(13,2)) as prior_deferral_rate, rate_escalator_frequency, cast(rate_escalator_inc_percent as DECIMAL(7,2)) as rate_escalator_inc_percent, cast(rate_escalator_max_percent as DECIMAL(7,2)) as rate_escalator_max_percent, cast(source_adj_vest_percent as DECIMAL(6,3)) as source_adj_vest_percent, cast(supplemental_def_dollar_prior as DECIMAL(13,2)) as supplemental_deferral_dollar_prior, 'VRP-SP' as source_system, cast(source_cycle_date as DATE) as source_cycle_date,cast(null as DATE) as source_processing_date, cast(actual_deferral_amount as DECIMAL(11,2)) as actual_deferral_amount, cast(null as varchar(20)) as deferral_rate_actual, cast(catch_up_deferral_amount as DECIMAL(11,2)) as catchup_deferral_amount, cast(null as VARCHAR(30)) as money_source_name from exn_xxewre01_xxewrpps_jb")

    ng_merged_df = merge_dataframes(
        spark=spark,
        df1=exn_xxewre01_xxewrpps_ng_df,
        df2=super_omni_newr_partacctms_daily_ng_dat_df,
        primary_key=primary_key
    )

    jb_merged_df = merge_dataframes(
        spark=spark,
        df1=exn_xxewre01_xxewrpps_jb_df,
        df2=super_omni_newr_partacctms_daily_jb_dat_df,
        primary_key=primary_key
    )

    transform_df = ng_merged_df.unionByName(jb_merged_df)

    return transform_df