
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("select z.client_id, z.source_cycle_date, cl.client_name, z.total_client_balance as cash_value_amount, z.client_loan_balance as total_loan_amount, z.sdba_cash_value_amount from ( select coalesce(t1.client_id, '-9999') as client_id, coalesce(t1.source_cycle_date, current_date()) as source_cycle_date, cast(t1.total_client_balance as DECIMAL(17, 2)) as total_client_balance, cast(t1.sdba_cash_value_amount as DECIMAL(17, 2)) as sdba_cash_value_amount, cast(t2.client_loan_balance as DECIMAL(17, 2)) as client_loan_balance, cast(null as VARCHAR(36)) as client_key from ( select pcb.client_id, pcb.source_cycle_date, sum(coalesce(pcb.cash_value_amount, 0.00)) as total_client_balance, sum(coalesce(pcb.sdba_cash_value_amount, 0.00)) as sdba_cash_value_amount from participant_core_balance_monthly pcb group by pcb.client_id, pcb.source_cycle_date ) t1 left outer join ( select k.client_id, sum(coalesce(k.client_loan_balance, 0.00)) as client_loan_balance from ( select pl.client_id, case when pl.source_system = 'PREMIER' THEN outstanding_principal_balance ELSE loan_balance end as client_loan_balance from participant_loan pl ) k group by k.client_id ) t2 on coalesce(t1.client_id, -9999) = coalesce(t2.client_id, -9999) ) z left outer join client cl on coalesce(z.client_id, -9999) = coalesce(cl.client_id, -9999) inner join newr_transform.calendar_helper cal on z.source_cycle_date = cal.qtr_last_business_day")

    return consumption_df