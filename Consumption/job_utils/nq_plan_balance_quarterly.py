
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("select coalesce(q1.client_id, '-9999') as client_id, coalesce(q1.plan_number, '-9999') as plan_number, q1.source_cycle_date as source_cycle_date,  fund_units,  fund_amount  from (select  coalesce(t1.client_id, '-9999') as client_id, coalesce(t1.plan_number, '-9999') as plan_number,t1.source_cycle_date as source_cycle_date,  CAST(SUM(t1.total_shares) AS DECIMAL(17, 4)) as fund_units,       CAST(SUM(t1.total_balance) AS DECIMAL(18, 2)) as fund_amount     from ( SELECT coalesce(np.client_id, '-9999') as client_id,  coalesce(np.plan_number, '-9999') as plan_number,           coalesce(npf.total_shares, 0.0000) as total_shares, coalesce(npf.total_balance, 0.00) as total_balance,           coalesce(             CAST(npf.source_cycle_date AS DATE), current_date() -1 ) as source_cycle_date from nq_plan as np RIGHT OUTER JOIN nq_participant_fund_monthly as npf ON coalesce(npf.plan_number, '-9999') = coalesce(np.plan_number, '-9999')) as t1  group by   t1.client_id, t1.plan_number,  t1.source_cycle_date ) q1 inner join calendar_helper cal on cal.qtr_last_business_day = q1.source_cycle_date  ")

    return consumption_df