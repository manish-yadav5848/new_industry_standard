from pyspark.sql.functions import col, when, lit, coalesce

def identify_invalid_plan_number(df):
    invalid_plan_id_lb = '000001'
    invalid_plan_id_ub = '000040'

    if 'plan_id' in df.columns:
        plan_column_name = 'plan_id'
    elif 'plan_number' in df.columns:
        plan_column_name = 'plan_number'
    else:
        plan_column_name = None

    if plan_column_name is not None:
        df = df.withColumn("to_drop",
                           when((col(plan_column_name).between(invalid_plan_id_lb, invalid_plan_id_ub)) |
                                ((col("client_id") == "NG") & (col(plan_column_name).isin('999999', '999998', '999997'))),
                                coalesce(lit(True), col("to_drop")))
                           .otherwise(col("to_drop"))) \
               .withColumn("drop_record_remarks",
                           when((col(plan_column_name).between(invalid_plan_id_lb, invalid_plan_id_ub)) |
                                ((col("client_id") == "NG") & (col(plan_column_name).isin('999999', '999998', '999997'))),
                                coalesce(lit("invalid plan id"), col("drop_record_remarks")))
                           .otherwise(col("drop_record_remarks")))

    return df
