 
drop table NEWR_REPOSB.PARTICIPANT_BALANCE;
drop table NEWR_REPOSB.PARTICIPANT_BALANCE_delta;
drop table NEWR_REPOSB.PARTICIPANT_BALANCE_monthly;
drop table NEWR_REPOSB.PARTICIPANT_BALANCE_monthly_delta;
drop table NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly;
drop table NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly_delta;

-- participant_balance
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
CONSTRAINT PK_PArticipant_balance PRIMARY KEY 
(
plan_number,
participant_id,
client_id,
source_cycle_date
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA;	





--- GRANT PARTICIPANT_BALANCE
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE TO role_newr_repos_write;




-- PARTICIPANT_BALANCE_monthly
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE_monthly 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
CONSTRAINT PK_PARTICIPANT_BALANCE_monthly PRIMARY KEY 
(
plan_number,
participant_id,
client_id,
source_cycle_date
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA;




--- GRANT PARTICIPANT_BALANCE_monthly
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE_monthly TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE_monthly TO role_newr_repos_write;


-- PARTICIPANT_BALANCE_quarterly
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
CONSTRAINT PK_PARTICIPANT_BALANCE_quarterly PRIMARY KEY 
(
plan_number,
participant_id,
client_id,
source_cycle_date
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA;




--- GRANT PARTICIPANT_BALANCE_quarterly
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly TO role_newr_repos_write;



-- participant_balance_delta
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE_delta 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
DELTA_OP_IND VARCHAR(1)
)
TABLESPACE NEWR_REPOS_DATA;




--- GRANT PARTICIPANT_BALANCE_delta
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE_delta TO role_newr_repos_write;




-- PARTICIPANT_BALANCE_monthly_delta
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE_monthly_delta 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
DELTA_OP_IND VARCHAR(1)
)
TABLESPACE NEWR_REPOS_DATA;	





--- GRANT PARTICIPANT_BALANCE_monthly_delta
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE_monthly_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE_monthly_delta TO role_newr_repos_write;


-- PARTICIPANT_BALANCE_quarterly_delta
CREATE TABLE NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly_delta 
(
client_id	VARCHAR2(10 BYTE)	,
plan_number	VARCHAR2(25 BYTE)	,
participant_id	VARCHAR2(20 BYTE)	,
core_cash_value_amount	NUMBER(17, 2) 	,
noncore_cash_value_amount	NUMBER(17, 2) 	,
sdba_cash_value_amount	NUMBER(17, 2) 	,
loan_cash_value_amount	NUMBER(17, 2) 	,
life_cash_value_amount_monthly	NUMBER(17, 2) 	,
life_valuation_date	Date	,
ee_cash_value_amount	NUMBER(17, 2) 	,
er_cash_value_amount	NUMBER(17, 2) 	,
ytd_contributions	NUMBER(17, 2) 	,
source_cycle_date	Date,
DELTA_OP_IND VARCHAR(1)
)
TABLESPACE NEWR_REPOS_DATA;	





--- GRANT PARTICIPANT_BALANCE_quarterly_delta
GRANT SELECT ON NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly_delta TO role_newr_repos_write;
