from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    # super_omni_newr_histbal_ng_dat_df = spark.sql("SELECT concat(SOPB.plan_number,'-',SOPB.participant_id) as retirement_account_id,CAST( SOPB.contribution_current_cal_year AS DECIMAL(17, 2) ) AS ytd_contributions, CAST(SOPB.withdrawal_disbursements AS DECIMAL(15, 2)) AS disbursements_withdrawal, CAST(SOPB.vested_percent AS DECIMAL(15, 2)) AS vested_percent, coalesce(CAST(SOPB.vested_balance AS DECIMAL(15, 2)), 0) AS vested_balance, CAST(null AS DATE) AS valuation_date, CAST(SOPB.unit_price AS DECIMAL(19, 6)) AS share_price,  coalesce(CAST(SOPB.uninvested_balance AS DECIMAL(15, 2)), 0) AS uninvested_balance, CAST(SOPB.transfers_out AS DECIMAL(15, 2)) AS transfers_out, CAST(SOPB.transfers_in AS DECIMAL(15, 2)) AS transfers_in, CAST(SOPB.termination_disbursements AS DECIMAL(15, 2)) AS disbursements_termination, 'VRP-PB' as source_system, CAST(SOPB.source_cycle_date AS DATE) AS source_cycle_date, CASE WHEN SOPB.money_source = '' THEN '-9999' ELSE coalesce(SOPB.money_source, '-9999') END AS money_source, CAST(SOPB.shares_units_sold AS DECIMAL(13, 4)) AS shares_sold, CAST(SOPB.shares_units_receipted AS DECIMAL(13, 4)) AS shares_receipted, CAST(SOPB.shares_units_purchased AS DECIMAL(13, 4)) AS shares_purchased, CAST(SOPB.shares_units_forfeited AS DECIMAL(15, 2)) AS shares_forfeited, CAST(SOPB.shares_units_distributed AS DECIMAL(15, 2)) AS shares_distributed, coalesce(nullif(SOPB.plan_number, ''), '-9999') AS plan_number, CAST(SOPB.pending_debit_shares AS DECIMAL(15, 2)) AS shares_debit_pending, CAST(SOPB.pending_debit_cash AS DECIMAL(15, 2)) AS cash_debit_pending, CAST(SOPB.pending_credit_shares AS DECIMAL(15, 2)) AS shares_credit_pending, CAST(SOPB.pending_credit_cash AS DECIMAL(15, 2)) AS cash_credit_pending, CAST( SOPB.payment_attributable_contributions AS DECIMAL(15, 2) ) AS contrib_payment_attributable, coalesce(SOPB.participant_id, '-9999') AS participant_id,  CAST(SOPB.other_debits AS DECIMAL(15, 2)) AS debits_other, CAST(SOPB.number_of_units AS DECIMAL(17, 4)) AS total_shares, CAST(SOPB.net_contribution_current AS DECIMAL(15, 2)) AS current_net_contribution, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.pwe_money_source_name ELSE NULL END AS money_source_name, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.money_type_code ELSE NULL END AS money_type_description, CAST(SOPB.miscellanous_receipts AS DECIMAL(15, 2)) AS receipts_miscellanous, CAST(SOPB.miscellanous_debits AS DECIMAL(15, 2)) AS debits_miscellanous, CAST(SOPB.loan_repayment_principal AS DECIMAL(15, 2)) AS loan_repayment_principal, CAST(SOPB.loan_repayment_interest AS DECIMAL(15, 2)) AS loan_repayment_interest, CAST(SOPB.loan_issues AS DECIMAL(15, 2)) AS loan_issues, CAST(SOPB.insurance_premium_paid AS DECIMAL(15, 2)) AS insurance_premium_paid, CAST(SOPB.installment_disbursements AS DECIMAL(15, 2)) AS disbursements_installment, CASE WHEN SOPB.fund_iv = '90' THEN 'LN90' WHEN SOPB.fund_iv = '91' THEN 'LN91' ELSE coalesce(nullif(pf.fund_code, ''), '-9999') END AS fund_number, pf.fund_name AS fund_name, SOPB.fund_iv AS fund_iv, CAST(SOPB.forfeitures_debited AS DECIMAL(15, 2)) AS debited_forfeitures, CAST(SOPB.forfeitures_credited AS DECIMAL(15, 2)) AS credited_forfeitures, CAST(SOPB.fee_disbursements AS DECIMAL(15, 2)) AS disbursements_fee, CAST( SOPB.earnings_gain_loss_shares_unit AS DECIMAL(13, 4) ) AS shares_gain_loss_earnings, CAST(SOPB.earnings_dividend AS DECIMAL(15, 2)) AS dividend_earnings, CAST(SOPB.earnings_cash AS DECIMAL(15, 2)) AS cash_earnings, CAST(SOPB.conversions_out AS DECIMAL(15, 2)) AS conversions_out, CAST(SOPB.conversions_in AS DECIMAL(15, 2)) AS conversions_in, CAST(SOPB.contribution_gross AS DECIMAL(15, 2)) AS contribution_gross, CASE WHEN SOPB.contribution_current_fis_year = '0.00' THEN '0000' ELSE SOPB.contribution_current_fis_year END AS contribution_current_fis_year, CAST( SOPB.contribution_allocation_percent AS DECIMAL(13, 4) ) AS contribution_alloc_pct, coalesce(SOPB.client_id, '-9999') AS client_id, coalesce(CAST(cash_value AS DECIMAL(17, 2)), 0) AS cash_value_amount, CAST(SOPB.brokerage_account_trade_date AS DATE) AS sdba_trade_date, COALESCE( CAST( SOPB.brokerage_account_cash_value AS DECIMAL(15, 2) ), 0 ) AS sdba_cash_value_amount, CAST(SOPB.annual_dividend_amount AS DECIMAL(15, 4)) AS annual_dividend_amount, CAST(null AS VARCHAR(1)) AS action_code, CAST(SOPB.accrued_dividend_amount AS DECIMAL(15, 4)) AS accrued_dividend_amount, CAST(SOPB.trade_date AS DATE) AS trade_date, CAST(SOPB.net_dollars AS DECIMAL(15, 2)) AS net_dollars,cast(null as varchar(10)) as fund_margin_code, cast(null as varchar(10)) as account_fund_separate FROM super_omni_newr_histbal_ng_dat SOPB LEFT OUTER JOIN exn_xxewre01_xxewrpfd_ng AS pf ON SOPB.plan_number = pf.plan_number AND SOPB.fund_iv = pf.fund_iv LEFT OUTER JOIN pdab_money_source_helper_csv AS MS ON coalesce(SOPB.money_source, '-9999') = coalesce(MS.source_cd, '-9999')")

    # super_omni_newr_histbal_jb_dat_df = spark.sql("SELECT concat(SOPB.plan_number,'-',SOPB.participant_id) as retirement_account_id, coalesce(SOPB.client_id, '-9999') AS client_id, coalesce(SOPB.participant_id, '-9999') AS participant_id, coalesce(nullif(SOPB.plan_number, ''), '-9999') AS plan_number, SOPB.fund_iv AS fund_iv, CASE WHEN SOPB.money_source = '' THEN '-9999' ELSE coalesce(SOPB.money_source, '-9999') END AS money_source, CASE WHEN SOPB.fund_iv = '90' THEN 'LN90' WHEN SOPB.fund_iv = '91' THEN 'LN91' ELSE coalesce(nullif(pf.price_id, ''), '-9999') END AS fund_number, CAST( SOPB.contribution_current_cal_year AS DECIMAL(17, 2) ) AS ytd_contributions, CAST(SOPB.withdrawal_disbursements AS DECIMAL(15, 2)) AS disbursements_withdrawal, CAST(SOPB.vested_percent AS DECIMAL(15, 2)) AS vested_percent, coalesce(CAST(SOPB.vested_balance AS DECIMAL(15, 2)), 0) AS vested_balance, CAST(null AS DATE) AS valuation_date, CAST(SOPB.unit_price AS DECIMAL(19, 6)) AS share_price, coalesce(CAST(SOPB.uninvested_balance AS DECIMAL(15, 2)), 0) AS uninvested_balance, CAST(SOPB.transfers_out AS DECIMAL(15, 2)) AS transfers_out, CAST(SOPB.transfers_in AS DECIMAL(15, 2)) AS transfers_in, CAST(SOPB.termination_disbursements AS DECIMAL(15, 2)) AS disbursements_termination, 'VRP-SP' AS source_system, CAST(SOPB.source_cycle_date AS DATE) AS source_cycle_date, CAST(SOPB.shares_units_sold AS DECIMAL(13, 4)) AS shares_sold, CAST(SOPB.shares_units_receipted AS DECIMAL(13, 4)) AS shares_receipted, CAST(SOPB.shares_units_purchased AS DECIMAL(13, 4)) AS shares_purchased, CAST(SOPB.shares_units_forfeited AS DECIMAL(15, 2)) AS shares_forfeited, CAST(SOPB.shares_units_distributed AS DECIMAL(15, 2)) AS shares_distributed, CAST(SOPB.pending_debit_shares AS DECIMAL(15, 2)) AS shares_debit_pending, CAST(SOPB.pending_debit_cash AS DECIMAL(15, 2)) AS cash_debit_pending, CAST(SOPB.pending_credit_shares AS DECIMAL(15, 2)) AS shares_credit_pending, CAST(SOPB.pending_credit_cash AS DECIMAL(15, 2)) AS cash_credit_pending, CAST( SOPB.payment_attributable_contributions AS DECIMAL(15, 2) ) AS contrib_payment_attributable, CAST(SOPB.other_debits AS DECIMAL(15, 2)) AS debits_other, CAST(SOPB.number_of_units AS DECIMAL(17, 4)) AS total_shares, CAST(SOPB.net_contribution_current AS DECIMAL(15, 2)) AS current_net_contribution, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.pwe_money_source_name ELSE NULL END AS money_source_name, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.money_type_code ELSE NULL END AS money_type_description, CAST(SOPB.miscellanous_receipts AS DECIMAL(15, 2)) AS receipts_miscellanous, CAST(SOPB.miscellanous_debits AS DECIMAL(15, 2)) AS debits_miscellanous, CAST(SOPB.loan_repayment_principal AS DECIMAL(15, 2)) AS loan_repayment_principal, CAST(SOPB.loan_repayment_interest AS DECIMAL(15, 2)) AS loan_repayment_interest, CAST(SOPB.loan_issues AS DECIMAL(15, 2)) AS loan_issues, CAST(SOPB.insurance_premium_paid AS DECIMAL(15, 2)) AS insurance_premium_paid, CAST(SOPB.installment_disbursements AS DECIMAL(15, 2)) AS disbursements_installment, pf.fund_name AS fund_name, CAST(SOPB.forfeitures_debited AS DECIMAL(15, 2)) AS debited_forfeitures, CAST(SOPB.forfeitures_credited AS DECIMAL(15, 2)) AS credited_forfeitures, CAST(SOPB.fee_disbursements AS DECIMAL(15, 2)) AS disbursements_fee, CAST( SOPB.earnings_gain_loss_shares_unit AS DECIMAL(13, 4) ) AS shares_gain_loss_earnings, CAST(SOPB.earnings_dividend AS DECIMAL(15, 2)) AS dividend_earnings, CAST(SOPB.earnings_cash AS DECIMAL(15, 2)) AS cash_earnings, CAST(SOPB.conversions_out AS DECIMAL(15, 2)) AS conversions_out, CAST(SOPB.conversions_in AS DECIMAL(15, 2)) AS conversions_in, CAST(SOPB.contribution_gross AS DECIMAL(15, 2)) AS contribution_gross, CASE WHEN SOPB.contribution_current_fis_year = '0.00' THEN '0000' ELSE SOPB.contribution_current_fis_year END AS contribution_current_fis_year, CAST( SOPB.contribution_allocation_percent AS DECIMAL(13, 4) ) AS contribution_alloc_pct, coalesce(CAST(cash_value AS DECIMAL(17, 2)), 0) AS cash_value_amount, CAST(SOPB.brokerage_account_trade_date AS DATE) AS sdba_trade_date, COALESCE( CAST( SOPB.brokerage_account_cash_value AS DECIMAL(15, 2) ), 0 ) AS sdba_cash_value_amount, CAST(SOPB.annual_dividend_amount AS DECIMAL(15, 4)) AS annual_dividend_amount, CAST(null AS VARCHAR(1)) AS action_code, CAST(SOPB.accrued_dividend_amount AS DECIMAL(15, 4)) AS accrued_dividend_amount, CAST(SOPB.trade_date AS DATE) AS trade_date, CAST(SOPB.net_dollars AS DECIMAL(15, 2)) AS net_dollars, cast(null as varchar(10)) as fund_margin_code, cast(null as varchar(10)) as account_fund_separate FROM super_omni_newr_histbal_jb_dat SOPB LEFT OUTER JOIN exn_xxewre01_xxewrpfd_jb AS pf ON SOPB.plan_number = pf.plan_number AND SOPB.fund_iv = pf.fund_iv LEFT OUTER JOIN pdab_money_source_helper_csv AS MS ON coalesce(SOPB.money_source, '-9999') = coalesce(MS.source_cd, '-9999') where not (SOPB.client_id ='AB' and (pf.price_id  in ('','-9999') or pf.price_id is null) and cash_value=0)")

    exn_xxewre01_xxewrpcb_jb_df = spark.sql("SELECT concat(SOPB.plan_number,'-',SOPB.participant_id) as retirement_account_id, coalesce(SOPB.client_id, '-9999') AS client_id, coalesce(SOPB.participant_id, '-9999') AS participant_id, coalesce(nullif(SOPB.plan_number, ''), '-9999') AS plan_number, SOPB.fund_iv AS fund_iv, CASE WHEN SOPB.money_source = '' THEN '-9999' ELSE coalesce(SOPB.money_source, '-9999') END AS money_source, CASE WHEN SOPB.fund_iv = '90' THEN 'LN90' WHEN SOPB.fund_iv = '91' THEN 'LN91' ELSE coalesce(nullif(pf.price_id, ''), '-9999') END AS fund_number, CAST( SOPB.contribution_current_cal_year AS DECIMAL(17, 2) ) AS ytd_contributions, CAST(SOPB.withdrawal_disbursements AS DECIMAL(15, 2)) AS disbursements_withdrawal, CAST(SOPB.vested_percent AS DECIMAL(15, 2)) AS vested_percent, coalesce(CAST(SOPB.vested_balance AS DECIMAL(15, 2)), 0) AS vested_balance, CAST(null AS DATE) AS valuation_date, CAST(SOPB.unit_price AS DECIMAL(19, 6)) AS share_price, coalesce(CAST(SOPB.uninvested_balance AS DECIMAL(15, 2)), 0) AS uninvested_balance, CAST(SOPB.transfers_out AS DECIMAL(15, 2)) AS transfers_out, CAST(SOPB.transfers_in AS DECIMAL(15, 2)) AS transfers_in, CAST(SOPB.termination_disbursements AS DECIMAL(15, 2)) AS disbursements_termination, 'VRP-SP' AS source_system, CAST(SOPB.source_cycle_date AS DATE) AS source_cycle_date, CAST(SOPB.shares_units_sold AS DECIMAL(13, 4)) AS shares_sold, CAST(SOPB.shares_units_receipted AS DECIMAL(13, 4)) AS shares_receipted, CAST(SOPB.shares_units_purchased AS DECIMAL(13, 4)) AS shares_purchased, CAST(SOPB.shares_units_forfeited AS DECIMAL(15, 2)) AS shares_forfeited, CAST(SOPB.shares_units_distributed AS DECIMAL(15, 2)) AS shares_distributed, CAST(SOPB.pending_debit_shares AS DECIMAL(15, 2)) AS shares_debit_pending, CAST(SOPB.pending_debit_cash AS DECIMAL(15, 2)) AS cash_debit_pending, CAST(SOPB.pending_credit_shares AS DECIMAL(15, 2)) AS shares_credit_pending, CAST(SOPB.pending_credit_cash AS DECIMAL(15, 2)) AS cash_credit_pending, CAST( SOPB.payment_attributable_contributions AS DECIMAL(15, 2) ) AS contrib_payment_attributable, CAST(SOPB.other_debits AS DECIMAL(15, 2)) AS debits_other, CAST(SOPB.number_of_units AS DECIMAL(17, 4)) AS total_shares, CAST(SOPB.net_contribution_current AS DECIMAL(15, 2)) AS current_net_contribution, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.pwe_money_source_name ELSE NULL END AS money_source_name, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.money_type_code ELSE NULL END AS money_type_description, CAST(SOPB.miscellanous_receipts AS DECIMAL(15, 2)) AS receipts_miscellanous, CAST(SOPB.miscellanous_debits AS DECIMAL(15, 2)) AS debits_miscellanous, CAST(SOPB.loan_repayment_principal AS DECIMAL(15, 2)) AS loan_repayment_principal, CAST(SOPB.loan_repayment_interest AS DECIMAL(15, 2)) AS loan_repayment_interest, CAST(SOPB.loan_issues AS DECIMAL(15, 2)) AS loan_issues, CAST(SOPB.insurance_premium_paid AS DECIMAL(15, 2)) AS insurance_premium_paid, CAST(SOPB.installment_disbursements AS DECIMAL(15, 2)) AS disbursements_installment, pf.fund_name AS fund_name, CAST(SOPB.forfeitures_debited AS DECIMAL(15, 2)) AS debited_forfeitures, CAST(SOPB.forfeitures_credited AS DECIMAL(15, 2)) AS credited_forfeitures, CAST(SOPB.fee_disbursements AS DECIMAL(15, 2)) AS disbursements_fee, CAST( SOPB.earnings_gain_loss_shares_unit AS DECIMAL(13, 4) ) AS shares_gain_loss_earnings, CAST(SOPB.earnings_dividend AS DECIMAL(15, 2)) AS dividend_earnings, CAST(SOPB.earnings_cash AS DECIMAL(15, 2)) AS cash_earnings, CAST(SOPB.conversions_out AS DECIMAL(15, 2)) AS conversions_out, CAST(SOPB.conversions_in AS DECIMAL(15, 2)) AS conversions_in, CAST(SOPB.contribution_gross AS DECIMAL(15, 2)) AS contribution_gross, CASE WHEN SOPB.contribution_current_fis_year = '0.00' THEN '0000' ELSE SOPB.contribution_current_fis_year END AS contribution_current_fis_year, CAST( SOPB.contribution_allocation_percent AS DECIMAL(13, 4) ) AS contribution_alloc_pct, coalesce(CAST(cash_value AS DECIMAL(17, 2)), 0) AS cash_value_amount, CAST(SOPB.brokerage_account_trade_date AS DATE) AS sdba_trade_date, COALESCE( CAST( SOPB.brokerage_account_cash_value AS DECIMAL(15, 2) ), 0 ) AS sdba_cash_value_amount, CAST(SOPB.annual_dividend_amount AS DECIMAL(15, 4)) AS annual_dividend_amount, CAST(null AS VARCHAR(1)) AS action_code, CAST(SOPB.accrued_dividend_amount AS DECIMAL(15, 4)) AS accrued_dividend_amount, CAST(SOPB.trade_date AS DATE) AS trade_date, CAST(SOPB.net_dollars AS DECIMAL(15, 2)) AS net_dollars, cast(null as varchar(10)) as fund_margin_code, cast(null as varchar(10)) as account_fund_separate FROM exn_xxewre01_xxewrpcb_jb SOPB LEFT OUTER JOIN exn_xxewre01_xxewrpfd_jb AS pf ON SOPB.plan_number = pf.plan_number AND SOPB.fund_iv = pf.fund_iv LEFT OUTER JOIN pdab_money_source_helper_csv AS MS ON coalesce(SOPB.money_source, '-9999') = coalesce(MS.source_cd, '-9999') where not (SOPB.client_id ='AB' and (pf.price_id  in ('','-9999') or pf.price_id is null) and cash_value=0)")

    super_omni_newr_partsrcval_daily_ng_dat_df = spark.sql("SELECT concat(SOPB.plan_number,'-',SOPB.participant_id) as retirement_account_id,CAST( SOPB.contribution_current_cal_year AS DECIMAL(17, 2) ) AS ytd_contributions, CAST(SOPB.withdrawal_disbursements AS DECIMAL(15, 2)) AS disbursements_withdrawal, CAST(SOPB.vested_percent AS DECIMAL(15, 2)) AS vested_percent, coalesce(CAST(SOPB.vested_balance AS DECIMAL(15, 2)), 0) AS vested_balance, CAST(null AS DATE) AS valuation_date, CAST(SOPB.unit_price AS DECIMAL(19, 6)) AS share_price,  coalesce(CAST(SOPB.uninvested_balance AS DECIMAL(15, 2)), 0) AS uninvested_balance, CAST(SOPB.transfers_out AS DECIMAL(15, 2)) AS transfers_out, CAST(SOPB.transfers_in AS DECIMAL(15, 2)) AS transfers_in, CAST(SOPB.termination_disbursements AS DECIMAL(15, 2)) AS disbursements_termination, 'VRP-PB' as source_system, CAST(SOPB.source_cycle_date AS DATE) AS source_cycle_date, CASE WHEN SOPB.money_source = '' THEN '-9999' ELSE coalesce(SOPB.money_source, '-9999') END AS money_source, CAST(SOPB.shares_units_sold AS DECIMAL(13, 4)) AS shares_sold, CAST(SOPB.shares_units_receipted AS DECIMAL(13, 4)) AS shares_receipted, CAST(SOPB.shares_units_purchased AS DECIMAL(13, 4)) AS shares_purchased, CAST(SOPB.shares_units_forfeited AS DECIMAL(15, 2)) AS shares_forfeited, CAST(SOPB.shares_units_distributed AS DECIMAL(15, 2)) AS shares_distributed, coalesce(nullif(SOPB.plan_number, ''), '-9999') AS plan_number, CAST(SOPB.pending_debit_shares AS DECIMAL(15, 2)) AS shares_debit_pending, CAST(SOPB.pending_debit_cash AS DECIMAL(15, 2)) AS cash_debit_pending, CAST(SOPB.pending_credit_shares AS DECIMAL(15, 2)) AS shares_credit_pending, CAST(SOPB.pending_credit_cash AS DECIMAL(15, 2)) AS cash_credit_pending, CAST( SOPB.payment_attributable_contributions AS DECIMAL(15, 2) ) AS contrib_payment_attributable, coalesce(SOPB.participant_id, '-9999') AS participant_id,  CAST(SOPB.other_debits AS DECIMAL(15, 2)) AS debits_other, CAST(SOPB.number_of_units AS DECIMAL(17, 4)) AS total_shares, CAST(SOPB.net_contribution_current AS DECIMAL(15, 2)) AS current_net_contribution, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.pwe_money_source_name ELSE NULL END AS money_source_name, CASE WHEN MS.source_system = 'SUPEROMNI' THEN MS.money_type_code ELSE NULL END AS money_type_description, CAST(SOPB.miscellanous_receipts AS DECIMAL(15, 2)) AS receipts_miscellanous, CAST(SOPB.miscellanous_debits AS DECIMAL(15, 2)) AS debits_miscellanous, CAST(SOPB.loan_repayment_principal AS DECIMAL(15, 2)) AS loan_repayment_principal, CAST(SOPB.loan_repayment_interest AS DECIMAL(15, 2)) AS loan_repayment_interest, CAST(SOPB.loan_issues AS DECIMAL(15, 2)) AS loan_issues, CAST(SOPB.insurance_premium_paid AS DECIMAL(15, 2)) AS insurance_premium_paid, CAST(SOPB.installment_disbursements AS DECIMAL(15, 2)) AS disbursements_installment, CASE WHEN SOPB.fund_iv = '90' THEN 'LN90' WHEN SOPB.fund_iv = '91' THEN 'LN91' ELSE coalesce(nullif(pf.fund_code, ''), '-9999') END AS fund_number, pf.fund_name AS fund_name, SOPB.fund_iv AS fund_iv, CAST(SOPB.forfeitures_debited AS DECIMAL(15, 2)) AS debited_forfeitures, CAST(SOPB.forfeitures_credited AS DECIMAL(15, 2)) AS credited_forfeitures, CAST(SOPB.fee_disbursements AS DECIMAL(15, 2)) AS disbursements_fee, CAST( SOPB.earnings_gain_loss_shares_unit AS DECIMAL(13, 4) ) AS shares_gain_loss_earnings, CAST(SOPB.earnings_dividend AS DECIMAL(15, 2)) AS dividend_earnings, CAST(SOPB.earnings_cash AS DECIMAL(15, 2)) AS cash_earnings, CAST(SOPB.conversions_out AS DECIMAL(15, 2)) AS conversions_out, CAST(SOPB.conversions_in AS DECIMAL(15, 2)) AS conversions_in, CAST(SOPB.contribution_gross AS DECIMAL(15, 2)) AS contribution_gross, CASE WHEN SOPB.contribution_current_fis_year = '0.00' THEN '0000' ELSE SOPB.contribution_current_fis_year END AS contribution_current_fis_year, CAST( SOPB.contribution_allocation_percent AS DECIMAL(13, 4) ) AS contribution_alloc_pct, coalesce(SOPB.client_id, '-9999') AS client_id, coalesce(CAST(cash_value AS DECIMAL(17, 2)), 0) AS cash_value_amount, CAST(SOPB.brokerage_account_trade_date AS DATE) AS sdba_trade_date, COALESCE( CAST( SOPB.brokerage_account_cash_value AS DECIMAL(15, 2) ), 0 ) AS sdba_cash_value_amount, CAST(SOPB.annual_dividend_amount AS DECIMAL(15, 4)) AS annual_dividend_amount, CAST(null AS VARCHAR(1)) AS action_code, CAST(SOPB.accrued_dividend_amount AS DECIMAL(15, 4)) AS accrued_dividend_amount, CAST(SOPB.trade_date AS DATE) AS trade_date, CAST(SOPB.net_dollars AS DECIMAL(15, 2)) AS net_dollars,cast(null as varchar(10)) as fund_margin_code, cast(null as varchar(10)) as account_fund_separate FROM super_omni_newr_partsrcval_daily_ng_dat SOPB LEFT OUTER JOIN exn_xxewre01_xxewrpfd_ng AS pf ON SOPB.plan_number = pf.plan_number AND SOPB.fund_iv = pf.fund_iv LEFT OUTER JOIN pdab_money_source_helper_csv AS MS ON coalesce(SOPB.money_source, '-9999') = coalesce(MS.source_cd, '-9999')")

    nw00paap_nlarc_prdps_partval_pdab_data_df = spark.sql("select concat(plan_id,'-',part_account_num) as retirement_account_id,coalesce(q1.client_id,'-9999') AS client_id, CAST(NULL as DECIMAL(17, 2)) AS ytd_contributions,   CAST(null as DECIMAL(15, 2)) AS disbursements_withdrawal,   CAST(null as DECIMAL(15, 2)) AS vested_percent,   CAST(0 as DECIMAL(15, 2)) AS vested_balance,   CAST(PPV.valuation_date AS DATE) AS valuation_date,   CAST(PPV.unit_price AS DECIMAL(19, 6)) AS share_price,   coalesce(CAST(null as DECIMAL(15, 2)), 0) AS uninvested_balance,   CAST(null as DECIMAL(15, 2)) AS transfers_out,   CAST(null as DECIMAL(15, 2)) AS transfers_in,   CAST(null as DECIMAL(15, 2)) AS disbursements_termination,   PPV.part_aggr_src_syst_name AS source_system,   cast(substring(PPV.cycle_time_stamp, 1, 10) as date) as source_cycle_date,   CAST(null as DECIMAL(13, 4)) AS shares_sold,   CAST(null as DECIMAL(13, 4)) AS shares_receipted,   CAST(null as DECIMAL(13, 4)) AS shares_purchased,   CAST(null as DECIMAL(15, 2)) AS shares_forfeited,   CAST(null as DECIMAL(15, 2)) AS shares_distributed,  coalesce(nullif(PPV.plan_id, ''), '-9999') AS plan_number,   CAST(null as DECIMAL(15, 2)) AS shares_debit_pending,   CAST(null as DECIMAL(15, 2)) AS cash_debit_pending,   CAST(null as DECIMAL(15, 2)) AS shares_credit_pending,   CAST(null as DECIMAL(15, 2)) AS cash_credit_pending,   CAST(null as DECIMAL(15, 2)) AS contrib_payment_attributable,   coalesce(PPV.part_account_num, '-9999') AS participant_id,  CAST(null as DECIMAL(15, 2)) AS debits_other,   CAST(PPV.number_of_units AS DECIMAL(17, 4)) AS total_shares,   CAST(null as DECIMAL(15, 2)) AS current_net_contribution,   CASE     WHEN MS.source_system = 'PREMIER' THEN MS.pwe_money_source_name     ELSE NULL   END AS money_source_name,   coalesce(PPV.money_source_code, '-9999') AS money_source,   MS.user_area as money_type_description,   CAST(null as DECIMAL(15, 2)) AS receipts_miscellanous,   CAST(null as DECIMAL(15, 2)) AS debits_miscellanous,   CAST(null as DECIMAL(15, 2)) AS loan_repayment_principal,   CAST(null as DECIMAL(15, 2)) AS loan_repayment_interest,   CAST(null as DECIMAL(15, 2)) AS loan_issues,   CAST(null as DECIMAL(15, 2)) AS insurance_premium_paid,   CAST(null as DECIMAL(15, 2)) AS disbursements_installment,  coalesce(PPV.fund_number, '-9999') AS fund_number,   PPV.fund_name AS fund_name,   CAST(null as VARCHAR(5)) AS fund_iv,   CAST(null as DECIMAL(15, 2)) AS debited_forfeitures,   CAST(null as DECIMAL(15, 2)) AS credited_forfeitures,   CAST(null as DECIMAL(15, 2)) AS disbursements_fee,   CAST(null as DECIMAL(13, 4)) AS shares_gain_loss_earnings,   CAST(null as DECIMAL(15, 2)) AS dividend_earnings,   CAST(null as DECIMAL(15, 2)) AS cash_earnings,  CAST(null as DECIMAL(15, 2)) AS conversions_out,   CAST(null as DECIMAL(15, 2)) AS conversions_in,   CAST(null as DECIMAL(15, 2)) AS contribution_gross,   CAST(null as VARCHAR(4)) AS contribution_current_fis_year,   CAST(sf.allocation_pct as DECIMAL(13, 4)) AS contribution_alloc_pct,  coalesce(CAST(PPV.cash_value AS DECIMAL(17, 2)), 0) AS cash_value_amount,   CAST(null as DATE) AS sdba_trade_date,   CAST(0 as DECIMAL(15, 2)) AS sdba_cash_value_amount,   CAST(null as DECIMAL(15, 4)) AS annual_dividend_amount,   PPV.action_code AS action_code,   CAST(null as DECIMAL(15, 4)) AS accrued_dividend_amount,  CAST(null as DATE) AS trade_date,  CAST(null as DECIMAL(15, 2)) AS net_dollars,cast(null as varchar(10)) as fund_margin_code, cast(null as varchar(10)) as account_fund_separate from   nw00paap_nlarc_prdps_partval_pdab_data PPV left outer join nw00paap_nlarc_prdps_pdab_sffa_data sf on    coalesce(sf.plan_number, '-9999') = coalesce(PPV.plan_id, '-9999') and   coalesce(sf.policy_number, '-9999') = coalesce(PPV.part_account_num, '-9999') and coalesce(right(sf.fund_number,3), '-9999') = coalesce(PPV.fund_number, '-9999')    and coalesce(sf.money_source, '-9999') = coalesce(PPV.money_source_code, '-9999')   LEFT OUTER JOIN pdab_money_source_helper_csv AS MS ON coalesce(MS.asset_acct, '-9999') = coalesce(PPV.money_source_code, '-9999') left outer join nw00paap_nlarc_prdps_plan_pdab_data q1 on PPV.plan_id=trim(q1.plan_number)")

    transform_df = exn_xxewre01_xxewrpcb_jb_df.unionByName(super_omni_newr_partsrcval_daily_ng_dat_df).unionByName(nw00paap_nlarc_prdps_partval_pdab_data_df)

    return transform_df