
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    exn_xxadahst_xxadhdbx_ng_df = spark.sql("SELECT base_transaction_code, coalesce(client_id, '-9999') AS client_id, coalesce(plan_number, '-9999') AS plan_number, coalesce(participant_id, '-9999') AS participant_id, cast(trade_date AS DATE) AS trade_date, coalesce(cast(run_date AS DATE), CURRENT_DATE ()) AS run_date, coalesce(run_time, '-9999') AS run_time, reversal_reason, coalesce(cast(sequence_number AS INTEGER), '-9999') AS sequence_num, coalesce(cast(distribution_type AS INTEGER), - 9999) AS distribution_type, disbursement_reason, cast(distribution_amount AS DECIMAL(11, 2)), disbursement_reversal_date as reversal_date, alternate_payee_bank_account_number AS alt_payee_bank_account_number, cast(eligible_rollover_distribution_amount AS DECIMAL(11, 2)) AS elig_rollover_distrib_amount, cast(total_value_to_be_rolled AS DECIMAL(11, 2)), cast(cash_value_to_be_rolled AS DECIMAL(11, 2)), cast(number_of_shares_to_be_rolled AS DECIMAL(11, 2)) AS num_shares_to_be_rolled, market_value_of_shares_to_be_rolled AS mkt_value_shares_to_be_rolled, cast(cost_value_of_shares_to_be_rolled AS DECIMAL(11, 2)) AS cost_value_shares_to_be_rolled, tran_code_1 as trx_code, usage_code_group_level, other_share AS other_shares, cast(other_percent AS DECIMAL(13, 4)), cast(other_numeric AS INTEGER), cast(other_factor AS DECIMAL(17, 10)), cast(voucher_number AS INTEGER), trade_type, use_plan_year_flag, cast(associated_activity AS INTEGER), cast(sub_activity_code AS INTEGER), cast(state_tax_withheld AS DECIMAL(11, 2)), cast(mandatory_withholding_amount AS DECIMAL(11, 2)) AS mandatory_withholding_amount, cast(federal_tax_withheld AS DECIMAL(11, 2)) AS fed_tax_withheld, excess_distribution_type as fed_excess_distrib_type, related_participant_id, state_code, cast(five_year_participation_indicator AS INTEGER) AS five_year_partcip_indicat, cast(percent_of_split AS DECIMAL(5, 4)) as split_percent, cast(lump_sum_distribution_indicator AS INTEGER) AS lump_sum_distrib_indicat, cast(qvec_distribution_indicator AS INTEGER) as qvec_distrib_ind, federal_distribution_type AS fed_distribution_type, federal_averaging_benefit_exclusion_code AS fed_avg_benefit_exclusion_code, tran_reason_code, check_delivery_method, plan_code, cast(capital_gains_distribution_federal AS DECIMAL(11, 2)) AS fed_capital_gains, cast(ordinary_income_distributed_federal AS DECIMAL(11, 2)) AS fed_ordinary_income, cast(nontaxable_employee_contributions_earnings_distributed_federal AS DECIMAL(11, 2)) AS fed_nontax_ee_contrib_earn, cast(unrealized_gain_on_employer_securities_federal AS DECIMAL(11, 2)) AS fed_unreal_gain_er_securities, cast(percent_of_federal_tax_withheld AS DECIMAL(5, 4)) AS fed_tax_withheld_pct, federal_withholding_override_flag AS fed_withhold_override_flag, cast(federal_withholding_override_amount AS DECIMAL(11, 2)) AS fed_withhold_override_amount, cast(federal_tax_override_percent AS DECIMAL(5, 4)) AS fed_tax_override_percent, cast(federal_marital_status_override AS INTEGER) AS fed_marital_status_override, cast(federal_tax_exemptions_override AS INTEGER) AS fed_tax_exemptions_override, cast(state_marital_status_override AS INTEGER), electronic_payment_indicator, state_withholding_override_flag AS state_withhold_override_flag, cast(state_withholding_override_amount AS DECIMAL(11, 2)) AS state_withhold_override_amount, cast(state_withholding_override_percent AS DECIMAL(5, 4)) AS state_withhold_override_pct, percent_of_state_tax_withheld as state_tax_withheld_pct, cast(local_withholding_amount AS DECIMAL(11, 2)), cast(local_withholding_override_percent AS DECIMAL(5, 4)) AS local_withhold_override_pct, local_withholding_override_flag AS local_withhold_override_flag, cast(local_withholding_override_amount AS DECIMAL(11, 2)) AS local_withhold_override_amount, cast(local_withholding_percent AS DECIMAL(5, 4)), cast(local_marital_status_override AS INTEGER), cast(qvec_distribution_amount AS DECIMAL(11, 2)), cast(federal_tax_withheld_on_qvec_distribution AS DECIMAL(11, 2)) AS fed_tax_with_on_qvec_distrib, cast(state_tax_withheld_on_qvec_distribution AS DECIMAL(11, 2)) AS state_tax_with_on_qvec_distrib, cast(dividend_amount_distrbuted AS DECIMAL(11, 2)) AS dividend_amount_distributed, cast(check_number AS INTEGER), udf_code_3, cast(value_of_shares_sold AS DECIMAL(11, 2)) AS value_shares_sold, cast(cost_of_shares_sold AS DECIMAL(11, 2)) AS cost_shares_sold, cast(value_of_shares_distributed AS DECIMAL(11, 2)) AS value_shares_distributed, cost_of_shares_distributed_from_contributions AS cost_of_shares_contributed, cast(status_prior_to_disbursement AS INTEGER) as prior_status, check_address_line_1, check_address_line_2, check_address_line_3, check_address_city, check_address_state, check_address_zip_code, cast(posting_process_counter AS INTEGER) as post_num, cast(pre_1987_after_tax_contributions_distributed AS DECIMAL(11, 2)) AS pre87_aftax_contrib_distrib, cast(post_1986_after_tax_contributions_distributed AS DECIMAL(11, 2)) AS post86_aftax_contrib_distrib, cast(federal_tax_basis_cost AS DECIMAL(11, 2)) AS fed_tax_basis_cost, cast(loan_repaid_amount_non_distributable AS DECIMAL(11, 2)) AS loan_repaid_amount_non_distrib, cast(cost_of_shares_distributed_from_earnings AS DECIMAL(11, 2)) AS cost_of_shares_earned, cast(state_tax_basis_cost AS DECIMAL(11, 2)), cast(termination_date AS DATE), cast(capital_gains_distribution_state AS DECIMAL(11, 2)) AS state_capital_gains, cast(ordinary_income_distributed_state AS DECIMAL(11, 2)) AS state_ordinary_income, cast(nontaxable_employee_contributions_earnings_distributed_state AS DECIMAL(11, 2)) AS state_nontax_ee_contrib_earn, cast(unrealized_gain_on_employer_securities_state AS DECIMAL(11, 2)) AS state_unreal_gain_er_securities, tax_year, minimum_distribution_amount, cast(loss_on_return_of_aftertax_contributions_federal AS DECIMAL(11, 2)) AS fed_loss_return_afttax_contrib, cast(loss_on_return_of_after_tax_contributions_state AS DECIMAL(11, 2)) AS state_loss_return_afttax_contrib, alternate_payee_address_line_1 AS alt_payee_address_line_1, alternate_payee_address_line_2 AS alt_payee_address_line_2, alternate_payee_address_line_3 AS alt_payee_address_line_3, alternate_payee_address_city AS alt_payee_address_city, alternate_payee_address_state AS state_alt_payee_address, alternate_payee_address_zip_code AS alt_payee_address_zip_code, alternate_payee_address_alternate_name AS alt_payee_address_alt_name, alternate_payee_bank_account_number_1 AS alt_payee_bank_account, alternate_payee_bank_number AS alt_payee_bank_number, usage_codes, cast(supplied_mandatory_withholding_amount AS DECIMAL(11, 2)) AS supp_mandat_withhold_amount, cast(supplied_mandatory_withholding_percent AS DECIMAL(5, 4)) AS supp_mandat_withhold_percent, supplied_mandatory_withholding_method AS supp_mandat_withhold_method, cast(NULL AS VARCHAR(36)) AS client_key, cast(NULL AS VARCHAR(36)) AS participant_key, cast(NULL AS VARCHAR(36)) AS plan_key, cast(NULL AS DATE) AS source_processing_date FROM exn_xxadahst_xxadhdbx_ng")
    exn_xxadahst_xxadhdbx_ng_df = exn_xxadahst_xxadhdbx_ng_df.withColumn('source_system', lit('VRP-PB'))

    exn_xxadahst_xxadhdbx_jb_df = spark.sql("SELECT base_transaction_code, coalesce(client_id, '-9999') AS client_id, coalesce(plan_number, '-9999') AS plan_number, coalesce(participant_id, '-9999') AS participant_id, cast(trade_date AS DATE) AS trade_date, coalesce(cast(run_date AS DATE), CURRENT_DATE ()) AS run_date, coalesce(run_time, '-9999') AS run_time, reversal_reason, coalesce(cast(sequence_number AS INTEGER), '-9999') AS sequence_num, coalesce(cast(distribution_type AS INTEGER), - 9999) AS distribution_type, disbursement_reason, cast(distribution_amount AS DECIMAL(11, 2)), disbursement_reversal_date as reversal_date, alternate_payee_bank_account_number AS alt_payee_bank_account_number, cast(eligible_rollover_distribution_amount AS DECIMAL(11, 2)) AS elig_rollover_distrib_amount, cast(total_value_to_be_rolled AS DECIMAL(11, 2)), cast(cash_value_to_be_rolled AS DECIMAL(11, 2)), cast(number_of_shares_to_be_rolled AS DECIMAL(11, 2)) AS num_shares_to_be_rolled, market_value_of_shares_to_be_rolled AS mkt_value_shares_to_be_rolled, cast(cost_value_of_shares_to_be_rolled AS DECIMAL(11, 2)) AS cost_value_shares_to_be_rolled, tran_code_1 as trx_code, usage_code_group_level, other_share AS other_shares, cast(other_percent AS DECIMAL(13, 4)), cast(other_numeric AS INTEGER), cast(other_factor AS DECIMAL(17, 10)), cast(voucher_number AS INTEGER), trade_type, use_plan_year_flag, cast(associated_activity AS INTEGER), cast(sub_activity_code AS INTEGER), cast(state_tax_withheld AS DECIMAL(11, 2)), cast(mandatory_withholding_amount AS DECIMAL(11, 2)) AS mandatory_withholding_amount, cast(federal_tax_withheld AS DECIMAL(11, 2)) AS fed_tax_withheld, excess_distribution_type as fed_excess_distrib_type, related_participant_id, state_code, cast(five_year_participation_indicator AS INTEGER) AS five_year_partcip_indicat, cast(percent_of_split AS DECIMAL(5, 4)) as split_percent, cast(lump_sum_distribution_indicator AS INTEGER) AS lump_sum_distrib_indicat, cast(qvec_distribution_indicator AS INTEGER) as qvec_distrib_ind, federal_distribution_type AS fed_distribution_type, federal_averaging_benefit_exclusion_code AS fed_avg_benefit_exclusion_code, tran_reason_code, check_delivery_method, plan_code, cast(capital_gains_distribution_federal AS DECIMAL(11, 2)) AS fed_capital_gains, cast(ordinary_income_distributed_federal AS DECIMAL(11, 2)) AS fed_ordinary_income, cast(nontaxable_employee_contributions_earnings_distributed_federal AS DECIMAL(11, 2)) AS fed_nontax_ee_contrib_earn, cast(unrealized_gain_on_employer_securities_federal AS DECIMAL(11, 2)) AS fed_unreal_gain_er_securities, cast(percent_of_federal_tax_withheld AS DECIMAL(5, 4)) AS fed_tax_withheld_pct, federal_withholding_override_flag AS fed_withhold_override_flag, cast(federal_withholding_override_amount AS DECIMAL(11, 2)) AS fed_withhold_override_amount, cast(federal_tax_override_percent AS DECIMAL(5, 4)) AS fed_tax_override_percent, cast(federal_marital_status_override AS INTEGER) AS fed_marital_status_override, cast(federal_tax_exemptions_override AS INTEGER) AS fed_tax_exemptions_override, cast(state_marital_status_override AS INTEGER), electronic_payment_indicator, state_withholding_override_flag AS state_withhold_override_flag, cast(state_withholding_override_amount AS DECIMAL(11, 2)) AS state_withhold_override_amount, cast(state_withholding_override_percent AS DECIMAL(5, 4)) AS state_withhold_override_pct, percent_of_state_tax_withheld as state_tax_withheld_pct, cast(local_withholding_amount AS DECIMAL(11, 2)), cast(local_withholding_override_percent AS DECIMAL(5, 4)) AS local_withhold_override_pct, local_withholding_override_flag AS local_withhold_override_flag, cast(local_withholding_override_amount AS DECIMAL(11, 2)) AS local_withhold_override_amount, cast(local_withholding_percent AS DECIMAL(5, 4)), cast(local_marital_status_override AS INTEGER), cast(qvec_distribution_amount AS DECIMAL(11, 2)), cast(federal_tax_withheld_on_qvec_distribution AS DECIMAL(11, 2)) AS fed_tax_with_on_qvec_distrib, cast(state_tax_withheld_on_qvec_distribution AS DECIMAL(11, 2)) AS state_tax_with_on_qvec_distrib, cast(dividend_amount_distrbuted AS DECIMAL(11, 2)) AS dividend_amount_distributed, cast(check_number AS INTEGER), udf_code_3, cast(value_of_shares_sold AS DECIMAL(11, 2)) AS value_shares_sold, cast(cost_of_shares_sold AS DECIMAL(11, 2)) AS cost_shares_sold, cast(value_of_shares_distributed AS DECIMAL(11, 2)) AS value_shares_distributed, cost_of_shares_distributed_from_contributions AS cost_of_shares_contributed, cast(status_prior_to_disbursement AS INTEGER) as prior_status, check_address_line_1, check_address_line_2, check_address_line_3, check_address_city, check_address_state, check_address_zip_code, cast(posting_process_counter AS INTEGER) as post_num, cast(pre_1987_after_tax_contributions_distributed AS DECIMAL(11, 2)) AS pre87_aftax_contrib_distrib, cast(post_1986_after_tax_contributions_distributed AS DECIMAL(11, 2)) AS post86_aftax_contrib_distrib, cast(federal_tax_basis_cost AS DECIMAL(11, 2)) AS fed_tax_basis_cost, cast(loan_repaid_amount_non_distributable AS DECIMAL(11, 2)) AS loan_repaid_amount_non_distrib, cast(cost_of_shares_distributed_from_earnings AS DECIMAL(11, 2)) AS cost_of_shares_earned, cast(state_tax_basis_cost AS DECIMAL(11, 2)), cast(termination_date AS DATE), cast(capital_gains_distribution_state AS DECIMAL(11, 2)) AS state_capital_gains, cast(ordinary_income_distributed_state AS DECIMAL(11, 2)) AS state_ordinary_income, cast(nontaxable_employee_contributions_earnings_distributed_state AS DECIMAL(11, 2)) AS state_nontax_ee_contrib_earn, cast(unrealized_gain_on_employer_securities_state AS DECIMAL(11, 2)) AS state_unreal_gain_er_securities, tax_year, minimum_distribution_amount, cast(loss_on_return_of_aftertax_contributions_federal AS DECIMAL(11, 2)) AS fed_loss_return_afttax_contrib, cast(loss_on_return_of_after_tax_contributions_state AS DECIMAL(11, 2)) AS state_loss_return_afttax_contrib, alternate_payee_address_line_1 AS alt_payee_address_line_1, alternate_payee_address_line_2 AS alt_payee_address_line_2, alternate_payee_address_line_3 AS alt_payee_address_line_3, alternate_payee_address_city AS alt_payee_address_city, alternate_payee_address_state AS state_alt_payee_address, alternate_payee_address_zip_code AS alt_payee_address_zip_code, alternate_payee_address_alternate_name AS alt_payee_address_alt_name, alternate_payee_bank_account_number_1 AS alt_payee_bank_account, alternate_payee_bank_number AS alt_payee_bank_number, usage_codes, cast(supplied_mandatory_withholding_amount AS DECIMAL(11, 2)) AS supp_mandat_withhold_amount, cast(supplied_mandatory_withholding_percent AS DECIMAL(5, 4)) AS supp_mandat_withhold_percent, supplied_mandatory_withholding_method AS supp_mandat_withhold_method, cast(NULL AS VARCHAR(36)) AS client_key, cast(NULL AS VARCHAR(36)) AS participant_key, cast(NULL AS VARCHAR(36)) AS plan_key, cast(NULL AS DATE) AS source_processing_date FROM exn_xxadahst_xxadhdbx_jb")
    exn_xxadahst_xxadhdbx_jb_df = exn_xxadahst_xxadhdbx_jb_df.withColumn('source_system', lit('VRP-SP'))

    transform_df = exn_xxadahst_xxadhdbx_ng_df.unionByName(exn_xxadahst_xxadhdbx_jb_df)

    return transform_df