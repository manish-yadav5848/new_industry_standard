
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    exn_xxadsumt_xxadhsfx_2_jb_df = spark.sql("SELECT client_id, plan_number, cast(source_cycle_date AS DATE), cast(total_enrollments AS INTEGER), cast(total_employee_before_tax_contributions_count AS INTEGER) AS total_emp_before_tax_contri_count, cast(total_employee_after_tax_contributions_count AS INTEGER) AS total_emp_after_tax_contri_count, cast(total_employer_contributions_count AS INTEGER) AS total_employer_contrib_count, cast(total_rollover_contributions_count AS INTEGER) AS total_rollover_contrib_count, cast(total_termination_distributions_with_rollover_count AS INTEGER) AS total_term_distrib_roll_count, cast(total_termination_distributions_with_rollover_not_rolled_amount AS DECIMAL(14, 2)) AS total_term_distrib_roll_not_roll, cast(total_termination_distributions_with_no_rollover_count AS INTEGER) AS total_term_distrib_no_roll_count, cast(total_termination_distributions_with_no_rollover_amount AS DECIMAL(14, 2)) AS total_term_distrib_no_roll_amount, cast(total_in_service_withdrawals_with_rollover_count AS INTEGER) AS total_insrvc_withd_with_roll_count, cast(total_in_service_withdrawals_with_rollover_rolled_amount AS DECIMAL(14, 2)) AS total_withd_roll_rolled_amount , cast(total_in_service_withdrawals_with_no_rollover_count AS INTEGER) AS total_insrvc_withd_no_roll_count, cast(total_in_service_withdrawals_with_no_rollover_amount AS DECIMAL(14, 2)) AS total_insrvc_withd_no_roll_amount, cast(total_hardship_withdrawals_count AS INTEGER) AS total_hardship_withdrawals_count, cast(total_hardship_withdrawals_amount AS DECIMAL(14, 2)) AS total_hardship_withdrawals_amount, total_installments_setup_count, cast(total_installment_distributions_by_check_count AS INTEGER) AS total_install_distrib_check_count, cast(total_installment_distributions_by_check_amount AS DECIMAL(14, 2)) AS total_install_distrib_check_amount, cast(total_installment_distributions_by_ach_count AS INTEGER) AS total_install_distrib_ach_count, cast(total_installment_distributions_by_ach_amount AS DECIMAL(14, 2)) AS total_install_distrib_ach_amount, cast(total_default_rollover_distributions_count AS INTEGER) AS total_default_roll_distrib_count, cast(total_default_rollover_distributions_amount AS DECIMAL(14, 2)) AS total_default_roll_distrib_amount, cast(total_deminimus_distributions_count AS INTEGER) AS total_deminimus_distrib_count, cast(total_deminimus_distributions_amount AS DECIMAL(14, 2)) AS total_deminimus_distrib_amount, cast(total_loan_issue_count AS INTEGER), cast(total_loan_reamortized_count AS INTEGER), cast(total_loan_defaults_deemed_distributions_count AS INTEGER) AS total_loan_def_deemed_distrib_count, cast(total_loan_repayments_count AS INTEGER), total_loan_payoff_count, cast(total_dividend_pass_thru_count AS INTEGER), cast(total_dividend_pass_thru_amount AS DECIMAL(14, 2)) AS total_dividend_pass_thru_amount, cast(total_dividend_reinvestments_count AS INTEGER) AS total_dividend_reinvestments_count, cast(total_dividend_reinvestments_amount AS DECIMAL(14, 2)) AS total_dividend_reinvestments_amount, cast(total_rebalance_transfers_count AS INTEGER) AS total_rebal_xfer_count, cast(total_fee_deductions_count AS INTEGER), cast(total_qdro_splits_count AS INTEGER), cast(total_beneficiary_splits_count AS INTEGER), cast(total_rmd_count AS INTEGER), cast(total_rmd_amount AS DECIMAL(14, 2)), div_sub_id, cast(total_cash_earnings_count AS DECIMAL(14, 2)), cast(total_cash_earnings_amount AS DECIMAL(14, 2)), cast(total_unreal_earn_count AS INTEGER), cast(total_unreal_earn_amount AS DECIMAL(14, 2)), cast(total_div_count AS INTEGER), cast(total_div_amount AS DECIMAL(14, 2)), cast(total_earn_base_fct_count AS INTEGER), cast(total_earn_base_fct_amount AS DECIMAL(14, 2)), cast(total_fee_count AS INTEGER), cast(total_fee_amount AS DECIMAL(14, 2)), cast(total_inter_ppt_to_count AS INTEGER), cast(total_inter_ppt_to_amount AS DECIMAL(14, 2)), cast(total_inter_ppt_frm_count AS INTEGER), cast(total_inter_ppt_frm_amount AS DECIMAL(14, 2)), cast(total_inter_ppt_rel_count AS INTEGER), cast(total_inter_ppt_rel_amount AS DECIMAL(14, 2)), cast(total_loan_reamrt_count AS INTEGER), cast(total_loan_reamrt_amount AS DECIMAL(14, 2)), cast(total_loan_ramrt_rt_count AS INTEGER), cast(total_loan_ramrt_rt_amount AS DECIMAL(14, 2)), cast(total_accord_int_count AS INTEGER), cast(total_accord_int_amount AS DECIMAL(14, 2)), cast(total_rtrn_excss_count AS INTEGER), cast(total_rtrn_excss_amount AS DECIMAL(14, 2)), cast(total_rtrn_excss_wd_count AS INTEGER), cast(total_rtrn_excss_wd_amount AS DECIMAL(14, 2)), cast(total_enrl_dem_count AS INTEGER), cast(total_in_service_withdrawals_with_rollover_not_rolled_amount AS DECIMAL(14, 2)) AS total_withd_roll_not_rolled_amount, cast(total_enrl_elec_count AS INTEGER), cast(total_dem_updt_count AS INTEGER), cast(total_inv_elec_count AS INTEGER), cast(total_termination_distributions_with_rollover_rolled_amount AS DECIMAL(14, 2)) AS total_term_distrib_roll_rolled, cast(total_loan_issue_amount AS DECIMAL(14, 2)) FROM exn_xxadsumt_xxadhsfx_2_jb")
    exn_xxadsumt_xxadhsfx_2_jb_df = exn_xxadsumt_xxadhsfx_2_jb_df.withColumn('source_system', lit('VRP-SP'))

    transform_df = exn_xxadsumt_xxadhsfx_2_jb_df

    return transform_df