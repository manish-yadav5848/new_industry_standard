
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def transform(spark: SparkSession, primary_key: list):

    consumption_df = spark.sql("select coalesce(base_transaction_code, '-9999') as base_transaction_code, coalesce(money_source, '-9999') as money_source, coalesce(plan_number, '-9999') as plan_number, run_date, rev_code, posting_process_counter, total_cash_amount, total_share_price, total_unit_shares, pay_period_end_date, trade_date from ( select case when tx.base_transaction_code = '' then '-9999' else tx.base_transaction_code end as base_transaction_code,case when t.money_source = '' then '-9999' else t.money_source end as money_source, coalesce(tx.posting_process_counter,'-9999') as posting_process_counter, coalesce(tx.rev_code, '-9999') as rev_code, case when t.plan_number = '' then '-9999' else t.plan_number end as plan_number, coalesce(t.run_date, current_date()) as run_date, tx.pay_period_end_date, tx.trade_date, coalesce( cast(t.total_cash_amount as decimal(17, 2)), '0.00' ) as total_cash_amount, coalesce( cast(t.total_share_price as decimal(17, 2)), '0.00' ) as total_share_price, coalesce(cast(t.total_shares as decimal(17, 4)), '0.00') as total_unit_shares from ( select  distinct(t.run_date) as as_on_date, t.plan_number as plan_number, t.money_source as money_source, t.run_date, calh.mo_last_business_day, sum(t.cash) over ( partition by t.plan_number, t.money_source, t.run_date order by t.run_date asc ) as total_cash_amount, sum(t.share_price) over ( partition by t.plan_number,  t.money_source, t.run_date order by t.run_date asc ) as total_share_price, sum(t.shares) over (  partition by t.plan_number, t.money_source, t.run_date order by  t.run_date asc ) as total_shares from txn t left outer join calendar_helper calh on t.run_date = calh.mo_last_business_day where calh.mo_last_business_day is null order by plan_number asc ) t left outer join txn tx on coalesce(tx.plan_number, '-9999') = coalesce(t.plan_number, '-9999') and coalesce(tx.money_source, '-9999') = coalesce(t.money_source, '-9999') and coalesce(tx.plan_number, '-9999') = coalesce(t.plan_number, '-9999') )")

    return consumption_df