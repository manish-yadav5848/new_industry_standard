
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("select coalesce(m1.client_id, -9999) as client_id, coalesce(nullif(m1.div_sub_id, ''), '-9999') as div_sub_id, coalesce(nullif(m1.plan_number, ''), -9999) as plan_number, coalesce(m1.source_cycle_date, current_date() -1) as source_cycle_date, coalesce(m1.money_source, '-9999') as money_source, m1.money_source_type_code, m1.ytd_contributions, m1.cash_value_amount, m1.vested_balance, cast(null as varchar(36)) as plan_key, cast(null as varchar(36)) as plan_source_key from ( select t1.div_sub_id, t1.plan_number, t1.client_id, t1.source_cycle_date, t1.money_source_type_code, case when t1.money_source = '' then '-9999' else t1.money_source end as money_source, CAST(t1.cash_value_amount AS DECIMAL(13, 2)) AS cash_value_amount, CAST(t1.vested_balance AS DECIMAL(13, 2)) AS vested_balance, cast(t1.ytd_contributions as Decimal(17, 2)) as ytd_contributions from ( select p1.plan_number, p1.source_cycle_date, p1.div_sub_id, p1.client_id, p1.money_source, p1.money_source_type_code, sum(p1.cash_value_amount) as cash_value_amount, sum(p1.vested_balance) as vested_balance, sum(p1.ytd_contributions) as ytd_contributions from ( select pcb.client_id, trim(p.div_sub_id) as div_sub_id, trim(pcb.plan_number) as plan_number, pcb.source_cycle_date, trim(pcb.money_source) as money_source, pcb.money_type_description as money_source_type_code, coalesce(pcb.cash_value, 0.00) as cash_value_amount, coalesce(pcb.vested_balance, 0.00) as vested_balance, coalesce(pcb.ytd_contributions, 0.00) as ytd_contributions from participant_core_balance pcb left outer join participant p on pcb.client_id = p.client_id and pcb.plan_number = p.plan_number and pcb.participant_id = p.participant_id ) p1 where div_sub_id not in ('', '-9999') group by p1.client_id, p1.plan_number, p1.source_cycle_date, p1.div_sub_id, p1.money_source, p1.money_source_type_code ) t1 ) m1 where div_sub_id not in ('-9999', '') order by plan_number, div_sub_id")

    return consumption_df