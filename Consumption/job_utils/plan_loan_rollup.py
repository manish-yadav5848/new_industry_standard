
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("select t3.plan_number, t3.client_id, t3.source_cycle_date, t3.total_loan_balance, t3.num_of_part_with_loans, t3.source_balance_amount, t3.total_num_of_loans, cast(null as Varchar(36)) as loan_key, cast(null as varchar(36)) as plan_key from ( select t2.plan_number, t2.client_id, t2.total_loan_balance, t2.num_of_part_with_loans, t2.source_cycle_date, t2.source_balance_amount, t2.total_num_of_loans from ( select q.num_of_part_with_loans, q.total_loan_balance, q.total_num_of_loans, q.source_balance_amount, coalesce(p.plan_number, -9999) as plan_number, coalesce(p.client_id, -9999) as client_id, coalesce(p.source_cycle_date, current_date() -1) as source_cycle_date from ( select coalesce(m.num_of_part_with_loans, 0) as num_of_part_with_loans, cast( coalesce(m.total_loan_balance, 0.00) as DECIMAL(13, 2) ) AS total_loan_balance, COALESCE(m.total_num_of_loans, 0) AS total_num_of_loans, t.source_balance_amount, m.client_id, m.plan_number from ( select plan_number, client_id, source_cycle_date, cast( coalesce(unit_share_balance, cash_balance, fund_balance) as DECIMAL(13, 2) ) as source_balance_amount from ( select plan_number, client_id, source_cycle_date, (unit_share_balance * fund_price) as fund_balance, cash_balance, unit_share_balance from ( select coalesce(pcb.plan_number, '-9999') as plan_number, coalesce(pcb.client_id, '-9999') as client_id, coalesce(pcb.source_cycle_date, current_date() -1) as source_cycle_date, coalesce(pcb.share_price, 0) as fund_price, coalesce(pcb.net_dollars, pcb.UNINVESTED_BALANCE, 0) as cash_balance, coalesce(pcb.total_shares, pcb.net_dollars, 0) as unit_share_balance from participant_core_balance as pcb ) ) ) t right outer join ( select count(distinct (participant_id)) as num_of_part_with_loans, count(distinct (loan_number)) as total_num_of_loans, plan_number, client_id, sum(total_loan_balance) as total_loan_balance from ( select participant_id, loan_number, plan_number, client_id, case when source_system = 'PREMIER' then outstanding_principal_balance else loan_balance end as total_loan_balance from participant_loan ppl ) where loan_number is not null group by plan_number, client_id ) m on coalesce(t.client_id, -9999) = coalesce(m.client_id, -9999) and coalesce(t.plan_number, -9999) = coalesce(m.plan_number, -9999) ) q left outer join plan p on coalesce(q.client_id, -9999) = coalesce(p.client_id, -9999) and coalesce(q.plan_number, -9999) = coalesce(p.plan_number, -9999) ) t2 ) t3")

    return consumption_df