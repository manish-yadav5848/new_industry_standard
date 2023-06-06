
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    participant_core_balance_monthly_df = spark.sql("select coalesce(m1.client_id, '-9999') as client_id, coalesce(m1.plan_number, '-9999') as plan_number, coalesce(m1.participant_id, '-9999') as participant_id, coalesce(m1.source_cycle_date, current_date() -1) as source_cycle_date, m1.total_shares, m1.core_cash_value_amount, m1.total_cash_amount, m1.ee_cash_value_amount, m1.er_cash_value_amount, m1.life_cash_value_amount, m1.sdba_cash_value_amount, coalesce(m1.loan_cash_value_amt, 0.00) as loan_cash_value_amount, m1.noncore_cash_value_amount, m1.ytd_contributions from ( select t1.source_cycle_date, t1.participant_id, t1.client_id, t1.plan_number, cast(t1.total_shares as DECIMAL(17, 4)) as total_shares, cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount, cast(t1.ee_cash_value_amount as DECIMAL(17, 2)) as ee_cash_value_amount, cast(t1.er_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount, cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions, cast( coalesce(t3.life_cash_value_amount, 0.00) as DECIMAL(13, 2) ) as life_cash_value_amount, cast(t1.sdba_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount, cast(t4.loan_cash_value_amt as DECIMAL(17, 2)) as loan_cash_value_amt, cast( ( coalesce(t3.life_cash_value_amount, 0.00) + coalesce(t1.sdba_cash_value_amount, 0.00) + coalesce(t4.loan_cash_value_amt, 0.00) + coalesce(t1.core_cash_value_amount, 0.00) ) as DECIMAL(17, 2) ) as total_cash_amount, cast( ( coalesce(t3.life_cash_value_amount, 0.00) + coalesce(t1.sdba_cash_value_amount, 0.00) + coalesce(t4.loan_cash_value_amt, 0.00) ) as DECIMAL(13, 2) ) as noncore_cash_value_amount from ( select p1.participant_id, p1.client_id, sum(p1.total_shares) as total_shares, p1.plan_number, p1.source_cycle_date, sum(coalesce(p1.ytd_contributions, 0.00)) as ytd_contributions, sum(p1.core_cash_value_amount) as core_cash_value_amount, sum(coalesce(p1.ee_cash_value_amount, 0.00)) as ee_cash_value_amount, sum(coalesce(p1.er_cash_value_amount, 0.00)) as er_cash_value_amount, sum(p1.sdba_cash_value_amount) as sdba_cash_value_amount from ( select pcb.participant_id, pcb.client_id, pcb.plan_number, pcb.total_shares, pcb.source_cycle_date, coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions, coalesce(pcb.cash_value_amount, 0.00) as core_cash_value_amount, case when money_type_description = 'EE' then cash_value_amount end as ee_cash_value_amount, case when money_type_description = 'ER' then cash_value_amount end as er_cash_value_amount, coalesce(pcb.sdba_cash_value_amount, 0.00) as sdba_cash_value_amount from participant_core_balance_monthly pcb ) p1 group by p1.participant_id, p1.client_id, p1.plan_number, p1.source_cycle_date ) t1 left outer join ( select pff.participant_id, pff.plan_number, sum(coalesce(pff.cash_value_amt, 0.00)) as life_cash_value_amount, pff.valuation_date from participant_life_fund_monthly pff group by pff.participant_id, pff.plan_number, pff.valuation_date ) t3 on coalesce(t1.participant_id, -9999) = coalesce(t3.participant_id, -9999) and coalesce(t1.plan_number, -9999) = coalesce(t3.plan_number, -9999) and coalesce(t1.source_cycle_date, current_date() -1) = coalesce(t3.valuation_date, current_date() -1) left outer join ( select k.participant_id, k.plan_number, k.source_cycle_date, k.client_id, sum(coalesce(k.loan_cash_value_amt, 0.00)) as loan_cash_value_amt from ( select pl.participant_id, pl.plan_number, pl.source_cycle_date, pl.client_id, case when pl.source_system = 'PREMIER' THEN outstanding_principal_balance ELSE loan_balance end as loan_cash_value_amt from participant_loan pl ) k group by k.client_id, k.participant_id, k.plan_number, k.source_cycle_date ) t4 on coalesce(t1.client_id, -9999) = coalesce(t4.client_id, -9999) and coalesce(t1.participant_id, -9999) = coalesce(t4.participant_id, -9999) and coalesce(t1.plan_number, -9999) = coalesce(t4.plan_number, -9999) and coalesce(t1.source_cycle_date, current_date() -1) = coalesce(t4.source_cycle_date, current_date() -1) ) m1")
    # rps_balance_df = spark.sql("select   coalesce(t1.client_id, '-9999') as client_id,   coalesce(nullif(t1.plan_number, ''), '-9999') as plan_number,   coalesce(t1.participant_id, '-9999') as participant_id,   t1.source_cycle_date as source_cycle_date,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount,   cast(0.00 as DECIMAL(17, 2)) as ee_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount,   cast(0.00 as DECIMAL(13, 2)) as life_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount,   cast(t1.total_shares as DECIMAL(17, 4)) as total_shares,   cast(0.00 as DECIMAL(17, 2)) as loan_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) AS total_cash_amount,   cast(t1.core_cash_value_amount as DECIMAL(13, 2)) as noncore_cash_value_amount,   cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) AS total_cash_amount from   (     select       p1.participant_id,       p1.client_id,       p1.plan_number,       p1.source_cycle_date,       sum(p1.core_cash_value_amount) as core_cash_value_amount,       sum(p1.ytd_contributions) as ytd_contributions,       sum(p1.total_shares) as total_shares     from       (         select           pcb.participant_id,           pcb.client_id,           pcb.plan_number,           pcb.source_cycle_date,           coalesce(pcb.cash_value, 0.00) as core_cash_value_amount,           coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions,            coalesce(pcb.number_of_units, 0.00) as total_shares          from           rps_balance pcb       ) p1     group by       p1.participant_id,       p1.client_id,       p1.plan_number,       p1.source_cycle_date   ) t1 inner join newr_transform.calendar_helper cal on t1.source_cycle_date = cal.mo_last_business_day")

    consumption_df = participant_core_balance_monthly_df

    return consumption_df