select plan_id,substring(collect_set(role_key)[0],1,3) as company_code from dss_dc_producerrole_daily_dat where plan_id in (select plan_number from super_omni_newr_plan_daily_ng_dat) group by plan_id
