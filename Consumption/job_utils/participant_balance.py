
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    participant_core_balance_df = spark.sql("select     coalesce(m1.client_id, '-9999') as client_id,   coalesce(nullif(m1.plan_number,''), '-9999') as plan_number,    coalesce(m1.participant_id, '-9999') as participant_id,   coalesce(m1.source_cycle_date, current_date()) as source_cycle_date,   m1.core_cash_value_amount,   m1.ytd_contributions,   m1.ee_cash_value_amount,   m1.er_cash_value_amount,   m1.life_cash_value_amount_monthly,   m1.sdba_cash_value_amount,   coalesce(m1.loan_cash_value_amt, 0.00) as loan_cash_value_amount,   m1.noncore_cash_value_amount,   m1.life_valuation_date,   cast(null as VARCHAR(36)) as participant_key,   cast(null as VARCHAR(36)) as client_key,   cast(null as VARCHAR(36)) as div_sub_key,   cast(null as VARCHAR(36)) as plan_key from   (         select           t1.source_cycle_date,           t1.participant_id,           t1.client_id,           t1.plan_number,           t5.valuation_date as life_valuation_date,           cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount,           cast(t1.ee_cash_value_amount as DECIMAL(17, 2)) as ee_cash_value_amount,           cast(t1.er_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount,           cast(t5.life_cash_value_amount as DECIMAL(13, 2)) as life_cash_value_amount_monthly,           cast(t1.sdba_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount,           cast(t4.loan_cash_value_amt as DECIMAL(17, 2)) as loan_cash_value_amt,           cast(             (               coalesce(t1.sdba_cash_value_amount, 0.00) + coalesce(t4.loan_cash_value_amt, 0.00) + coalesce(t5.life_cash_value_amount, 0.00)             ) as DECIMAL(13, 2)           ) as noncore_cash_value_amount,           cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions         from           (             select               p1.participant_id,               p1.client_id,               p1.plan_number,               p1.source_cycle_date,               sum(p1.core_cash_value_amount) as core_cash_value_amount,               sum(coalesce(ee_cash_value_amount, 0.00)) as ee_cash_value_amount,               sum(coalesce(er_cash_value_amount, 0.00)) as er_cash_value_amount,               sum(sdba_cash_value_amount) as sdba_cash_value_amount,               sum(p1.ytd_contributions) as ytd_contributions             from               (                 select                   pcb.participant_id,                   pcb.client_id,                   pcb.plan_number,                   pcb.source_cycle_date,                   coalesce(pcb.cash_value, 0.00) as core_cash_value_amount,case                     when money_type_description = 'EE' then cash_value                   end as ee_cash_value_amount,case                     when money_type_description = 'ER' then cash_value                   end as er_cash_value_amount,                   coalesce(pcb.brokerage_account_cash_value, 0.00) as sdba_cash_value_amount,                   coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions                 from                   participant_core_balance pcb               ) p1             group by               p1.participant_id,               p1.client_id,               p1.plan_number,               p1.source_cycle_date           ) t1           left outer join (             select               k.participant_id,               k.client_id,               k.plan_number,               sum(coalesce(k.loan_cash_value_amt, 0.00)) as loan_cash_value_amt             from               (                 select                   pl.participant_id,                   pl.plan_number,                   pl.client_id,                   case                     when pl.source_system = 'PREMIER' THEN outstanding_principal_balance                     ELSE loan_balance                   end as loan_cash_value_amt                 from                   participant_loan pl               ) k             group by              k.client_id,               k.participant_id,               k.plan_number                         ) t4 on coalesce(t1.participant_id, -9999) = coalesce(t4.participant_id, -9999)           and coalesce(t1.plan_number, -9999) = coalesce(t4.plan_number, -9999) and           coalesce(t1.client_id, -9999) = coalesce(t4.client_id, -9999)           left outer join (             select               sum(coalesce(cash_value_amt, 0)) as life_cash_value_amount,               plan_number,               participant_id,               valuation_date             from               participant_life_fund_monthly             group by               plan_number,               participant_id,               valuation_date           ) as t5 on coalesce(t1.participant_id, -9999) = coalesce(t5.participant_id, -9999)           and coalesce(t1.plan_number, -9999) = coalesce(t5.plan_number, -9999)       ) m1")

    rps_balance_df = spark.sql("select   coalesce(t1.client_id, '-9999') as client_id,   coalesce(nullif(t1.plan_number, ''), '-9999') as plan_number,   coalesce(t1.participant_id, '-9999') as participant_id,   t1.source_cycle_date as source_cycle_date,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as core_cash_value_amount,   cast(0.00 as DECIMAL(17, 2)) as ee_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as er_cash_value_amount,   cast(0.00 as DECIMAL(13, 2)) as life_cash_value_amount_monthly,   cast(t1.core_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount,   cast(0.00 as DECIMAL(17, 2)) as loan_cash_value_amount,   cast(t1.core_cash_value_amount as DECIMAL(13, 2)) as noncore_cash_value_amount,   cast(t1.ytd_contributions as DECIMAL(17, 2)) as ytd_contributions,   cast(null as date) as life_valuation_date,   cast(null as VARCHAR(36)) as participant_key,   cast(null as VARCHAR(36)) as client_key,   cast(null as VARCHAR(36)) as div_sub_key,   cast(null as VARCHAR(36)) as plan_key from              (         select           p1.participant_id,           p1.client_id,           p1.plan_number,           p1.source_cycle_date,           sum(p1.core_cash_value_amount) as core_cash_value_amount,           sum(p1.ytd_contributions) as ytd_contributions         from           (             select               pcb.participant_id,               pcb.client_id,               pcb.plan_number,               pcb.source_cycle_date,               coalesce(pcb.cash_value, 0.00) as core_cash_value_amount,                           coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions             from               rps_balance pcb           ) p1         group by           p1.participant_id,           p1.client_id,           p1.plan_number,           p1.source_cycle_date       ) t1")

    consumption_df = participant_core_balance_df.unionByName(rps_balance_df)

    return consumption_df