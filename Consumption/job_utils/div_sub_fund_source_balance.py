
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("SELECT t1.client_id, t1.plan_number, coalesce(nullif(t1.div_sub_id, ''), '-9999') AS div_sub_id, coalesce(nullif(t1.fund_number, ''), '-9999') AS fund_number, c2.fund_iv AS fund_iv, t1.money_source, t1.source_cycle_date, cast(t1.core_cash_value_amount AS Decimal(17, 2)) AS cash_value_amount, cast(t1.vested_balance AS Decimal(17, 2)) AS vested_balance, cast(t1.total_units AS DECIMAL(17, 4)) AS total_units, case when t1.fund_number = '-9999' then cast('0' as decimal(17, 4)) else cast(t1.unit_price [0] AS DECIMAL(17, 4)) end AS unit_price, cast(t1.ytd_contributions AS DEcimal(17, 2)) AS ytd_contributions, cast(null AS varchar(36)) AS plan_source_key FROM ( SELECT coalesce(client_id, '-9999') AS client_id, coalesce(nullif(plan_number, ''), '-9999') AS plan_number, coalesce(nullif(div_sub_id, ''), '-9999') AS div_sub_id, coalesce(fund_number, '-9999') AS fund_number, fund_iv, coalesce(nullif(money_source, ''), '-9999') AS money_source, coalesce(source_cycle_date, current_date() -1) AS source_cycle_date, sum(coalesce(cash_value_amount, 0)) AS core_cash_value_amount, sum(coalesce(vested_balance, 0)) AS vested_balance, sum(coalesce(total_shares, 0.00)) AS total_units, collect_set(unit_price) AS unit_price, sum(coalesce(ytd_contributions, 0)) AS ytd_contributions FROM ( SELECT trim(pcb.client_id) AS client_id, trim(pcb.plan_number) AS plan_number, trim(p.div_sub_id) AS div_sub_id, pcb.source_cycle_date, trim(pcb.money_source) AS money_source, pcb.fund_iv, pcb.cash_value_amount, pcb.vested_balance, pcb.ytd_contributions, pcb.share_price AS unit_price, pcb.total_shares, trim(pcb.fund_number) AS fund_number FROM participant_core_balance pcb left outer JOIN participant p ON pcb.client_id = p.client_id AND pcb.plan_number = p.plan_number AND pcb.participant_id = p.participant_id ) GROUP BY client_id, plan_number, div_sub_id, fund_number, money_source, source_cycle_date, fund_iv ) t1 left outer JOIN ( SELECT plan_number, fund_number, client_id, money_source, fund_iv, count(1) FROM participant_core_balance c2 GROUP BY plan_number, fund_number, client_id, money_source, fund_iv ) c2 ON t1.plan_number = c2.plan_number AND coalesce(nullif(t1.fund_number, ''), '-9999') = coalesce(nullif(c2.fund_number, ''), '-9999') AND t1.client_id = c2.client_id AND t1.money_source = c2.money_source WHERE t1.div_sub_id NOT IN ('', '-9999')")

    return consumption_df
