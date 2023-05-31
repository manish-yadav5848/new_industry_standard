
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    participant_core_balance_monthly_df = spark.sql("select coalesce(m.client_id, '-9999') as client_id, coalesce(m.plan_number, '-9999') as plan_number, coalesce(m.source_cycle_date, current_date() -1) as source_cycle_date, m.core_cash_value_amount, m.ee_cash_value_amount, m.er_cash_value_amount, m.life_cash_value_amount, m.sdba_cash_value_amount, m.loan_cash_value_amt as loan_cash_value_amount, m.noncore_cash_value_amount, m.ytd_contributions, m.total_shares, cast(m.allocated_participant_count as INTEGER) as allocated_participant_count, cast(m.active_participant_count as INTEGER) as active_participant_count, cast(m.participant_count as INTEGER) as participant_count, cast( ( m.core_cash_value_amount + m.noncore_cash_value_amount ) as DECIMAL(17, 2) ) AS total_cash_amount, cast(null as VARCHAR(36)) as plan_key from ( select t1.source_cycle_date, t1.client_id, t1.plan_number, cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount, cast(t1.ee_cash_value_amount as DECIMAL(17, 2)) as ee_cash_value_amount, cast(t1.er_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount, cast( coalesce(t3.life_cash_value_amount, 0.00) as DECIMAL(13, 2) ) as life_cash_value_amount, cast(t1.sdba_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount, cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions, cast(t4.loan_cash_value_amt as DECIMAL(17, 2)) as loan_cash_value_amt, cast( ( coalesce(t3.life_cash_value_amount, 0.00) + coalesce(t1.sdba_cash_value_amount, 0.00) + coalesce(t4.loan_cash_value_amt, 0.00) ) as DECIMAL(13, 2) ) as noncore_cash_value_amount, cast(coalesce(t1.total_shares, 0.00) as DECIMAL(17, 4)) as total_shares, t5.participant_count, t5.allocated_participant_count, t5.active_participant_count from ( select p1.client_id, p1.plan_number, p1.source_cycle_date, sum(p1.core_cash_value_amount) as core_cash_value_amount, sum(coalesce(ee_cash_value_amount, 0.00)) as ee_cash_value_amount, sum(coalesce(er_cash_value_amount, 0.00)) as er_cash_value_amount, sum(sdba_cash_value_amount) as sdba_cash_value_amount, sum(ytd_contributions) as ytd_contributions, sum(total_shares) as total_shares from ( select pcb.client_id, pcb.plan_number, pcb.source_cycle_date, coalesce(pcb.cash_value_amount, 0.00) as core_cash_value_amount, coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions, case when money_type_description = 'EE' then cash_value_amount end as ee_cash_value_amount, case when money_type_description = 'ER' then cash_value_amount end as er_cash_value_amount, coalesce(pcb.sdba_cash_value_amount, 0.00) as sdba_cash_value_amount, coalesce(pcb.total_shares, 0.00) as total_shares from participant_core_balance_monthly pcb ) p1 group by p1.client_id, p1.plan_number, p1.source_cycle_date ) t1 left outer join ( select pff.plan_number, sum(coalesce(pff.cash_value_amt, 0.00)) as life_cash_value_amount, pff.valuation_date from participant_life_fund_monthly pff group by pff.plan_number, pff.valuation_date ) t3 on coalesce(t1.plan_number, -9999) = coalesce(t3.plan_number, -9999) and coalesce(t1.source_cycle_date, current_date() -1) = coalesce(t3.valuation_date, current_date() -1) left outer join ( select k.client_id, k.plan_number, k.source_cycle_date, sum(coalesce(k.loan_cash_value_amt, 0.00)) as loan_cash_value_amt from ( select pl.client_id, pl.plan_number, pl.source_cycle_date, case when pl.source_system = 'PREMIER' THEN outstanding_principal_balance ELSE loan_balance end as loan_cash_value_amt from participant_loan pl ) k group by k.plan_number, k.source_cycle_date, k.client_id ) t4 on coalesce(t1.client_id, -9999) = coalesce(t4.client_id, -9999) and coalesce(t1.plan_number, -9999) = coalesce(t4.plan_number, -9999) and coalesce(t1.source_cycle_date, current_date() -1) = coalesce(t4.source_cycle_date, current_date() -1) left outer join ( select plan_number, client_id, count( distinct ( case when source_system = 'VRP-PB' OR source_system = 'VRP_SP' then case when PARTICIPANT_ACCOUNT_TYPE_CODE = 'ALLOC' then participant_id end when source_system = 'PREMIER' then participant_id end ) ) as allocated_participant_count, count( distinct ( case when source_system = 'VRP-PB' or source_system = 'VRP-SP' then case when PARTICIPANT_STATUS <= 16 then participant_id end when source_system = 'PREMIER' then case when PARTICIPANT_STATUS = 'A' then participant_id end end ) ) as Active_participant_count, count(distinct (participant_id)) as participant_count from participant group by plan_number, client_id ) as t5 On coalesce(t1.plan_number, -9999) = coalesce(t5.plan_number, -9999) ) m")

    # rps_balance_df = spark.sql("select  coalesce(t1.client_id, '-9999') as client_id,   coalesce(nullif(t1.plan_number, ''), '-9999') as plan_number,   t1.source_cycle_date as source_cycle_date,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount,   cast(t1.total_shares as DECIMAL(17, 4)) as total_shares,   cast(0.00 as DECIMAL(17, 2)) as ee_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount,   cast(0.00 as DECIMAL(13, 2)) as life_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount,   cast(0.00 as DECIMAL(17, 2)) as loan_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(13, 2)) as noncore_cash_value_amount,   cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions,   cast(c1.participant_count as integer) as participant_count,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) AS total_cash_amount,   cast(0 as integer) as active_participant_count,   cast(0 as integer) as allocated_participant_count,   cast(null as VARCHAR(36)) as plan_key from   (     select       p1.client_id,       p1.plan_number,       p1.source_cycle_date,       sum(p1.core_cash_value_amount) as core_cash_value_amount,       sum(p1.ytd_contributions) as ytd_contributions,       sum(p1.total_shares) as total_shares     from       (         select           pcb.client_id,           pcb.plan_number,           pcb.source_cycle_date,           coalesce(pcb.cash_value, 0.00) as core_cash_value_amount,           coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions,           coalesce(pcb.number_of_units, 0.00) as total_shares         from           rps_balance pcb       ) p1     group by       p1.client_id,       p1.plan_number,       p1.source_cycle_date   ) t1   left outer join (     select       plan_number,       count(distinct(participant_id)) as participant_count     from       participant     group by       plan_number   ) as c1 on coalesce(t1.plan_number, -9999) = coalesce(c1.plan_number, -9999) inner join newr_transform.calendar_helper cal on t1.source_cycle_date = cal.mo_last_business_day")

    consumption_df = participant_core_balance_monthly_df

    return consumption_df