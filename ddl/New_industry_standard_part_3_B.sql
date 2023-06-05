 
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


grant  SELECT on NEWR_REPOSB.PARTICIPANT_BALANCE_quarterly to WEALTH_CENTRAL with  grant  option;
grant  SELECT on NEWR_REPOSB.PARTICIPANT_BALANCE_monthly to WEALTH_CENTRAL with  grant  option;
grant  SELECT on NEWR_REPOSB.participant_balance to WEALTH_CENTRAL with  grant  option;


drop table NEWR_REPOSB.TABLE PART_SOURCE_TRANSFER_BALANCE;
drop table NEWR_REPOSB.TABLE PART_SOURCE_TRANSFER_BALANCE_delta;
--part_source_transfer_balance

CREATE TABLE NEWR_REPOSB.PARTICIPANT_SOURCE_TRANSFER_BALANCE 
(
client_id VARCHAR(10) ,
plan_number VARCHAR(25) ,
participant_id VARCHAR(17) ,
transfer_balance_seq_number NUMBER(19, 0) ,
from_fund_id VARCHAR(3) ,
to_fund_id VARCHAR(3) ,
transfer_amount DECIMAL(14,2) ,
allocation_percent DECIMAL(7,4) ,
reversal_type_flag VARCHAR(1) ,
reversal_run_date DATE ,
source_cycle_date DATE ,
usage_code_1 VARCHAR(1) ,
usage_code_2 VARCHAR(1) ,
usage_code_3 VARCHAR(3) ,
usage_code_4 VARCHAR(4) ,
usage_code_5 VARCHAR(1) ,
activity_type VARCHAR(5) ,
source_month_end_date DATE ,
source_system VARCHAR(40) ,
CONSTRAINT PK_PART_SOURCE_TRANSFER_BALANCE PRIMARY KEY 
(
  CLIENT_ID 
, PARTICIPANT_ID 
, transfer_balance_seq_number 
, PLAN_NUMBER 
, SOURCE_CYCLE_DATE 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;

CREATE TABLE NEWR_REPOSB.PARTICIPANT_SOURCE_TRANSFER_BALANCE_DELTA 
(
  client_id VARCHAR(10) ,
plan_number VARCHAR(25) ,
participant_id VARCHAR(17) ,
transfer_balance_seq_number NUMBER(19, 0) ,
from_fund_id VARCHAR(3) ,
to_fund_id VARCHAR(3) ,
transfer_amount DECIMAL(14,2) ,
allocation_percent DECIMAL(7,4) ,
reversal_type_flag VARCHAR(1) ,
reversal_run_date DATE ,
source_cycle_date DATE ,
usage_code_1 VARCHAR(1) ,
usage_code_2 VARCHAR(1) ,
usage_code_3 VARCHAR(3) ,
usage_code_4 VARCHAR(4) ,
usage_code_5 VARCHAR(1) ,
activity_type VARCHAR(5) ,
source_month_end_date DATE ,
source_system VARCHAR(40) ,
DELTA_OP_IND varchar2(1)
)
TABLESPACE NEWR_REPOS_DATA
;

-- TABLE: NEWR_REPOSB.part_source_transfer_balance
--

GRANT SELECT ON NEWR_REPOSB.participant_source_transfer_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_source_transfer_balance TO role_newr_repos_write;

-- TABLE: NEWR_REPOSB.part_source_transfer_balance
--

GRANT SELECT ON NEWR_REPOSB.participant_source_transfer_balance_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_source_transfer_balance_DELTA TO role_newr_repos_write;


grant  SELECT on NEWR_REPOSB.participant_source_transfer_balance to WEALTH_CENTRAL with  grant  option;



drop table NEWR_REPOSB.SOURCE_FUND_FUTURE_ALLOCATION;
CREATE TABLE NEWR_REPOSB.SOURCE_FUND_FUTURE_ALLOCATION 
(
  PLAN_NUMBER VARCHAR2(25 BYTE) NOT NULL 
, PARTICIPANT_ID VARCHAR2(15 BYTE) NOT NULL 
, FUND_NUMBER VARCHAR2(10 BYTE) NOT NULL
, SOURCE VARCHAR2(10 BYTE) NOT NULL 
, COMPANY_CODE VARCHAR2(3 BYTE) 
, ALLOCATION_PCT NUMBER(5, 2)
, SOCIAL_SECURITY_NUMBER VARCHAR2(9 BYTE) 
, SYSTEM_CODE VARCHAR2(7 BYTE) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE)
, PROCESS_DATE DATE, 
 CONSTRAINT PK_SOURCE_FND_FUTURE_ALLCATN PRIMARY KEY 
(
  FUND_NUMBER 
, PARTICIPANT_ID 
, SOURCE 
, PLAN_NUMBER 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
; 
 

-- TABLE: NEWR_REPOSB.source_fund_future_allocation
--

GRANT SELECT ON NEWR_REPOSB.source_fund_future_allocation TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.source_fund_future_allocation TO role_newr_repos_write;

drop table NEWR_REPOSB.SOURCE_FUND_FUTURE_ALLOCATION_DELTA;
CREATE TABLE NEWR_REPOSB.SOURCE_FUND_FUTURE_ALLOCATION_DELTA 
(
  PLAN_NUMBER VARCHAR2(25 BYTE) NOT NULL 
, PARTICIPANT_ID VARCHAR2(15 BYTE) NOT NULL 
, FUND_NUMBER VARCHAR2(10 BYTE) NOT NULL
, SOURCE VARCHAR2(10 BYTE) NOT NULL 
, COMPANY_CODE VARCHAR2(3 BYTE) 
, ALLOCATION_PCT NUMBER(5, 2)
, SOCIAL_SECURITY_NUMBER VARCHAR2(9 BYTE) 
, SYSTEM_CODE VARCHAR2(7 BYTE) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE)
, PROCESS_DATE DATE
, DELTA_OP_IND varchar2(1)
)
TABLESPACE NEWR_REPOS_DATA
; 
 

-- TABLE: NEWR_REPOSB.source_fund_future_allocation
--

GRANT SELECT ON NEWR_REPOSB.source_fund_future_allocation_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.source_fund_future_allocation_delta TO role_newr_repos_write;

grant  SELECT on NEWR_REPOSB.source_fund_future_allocation to WEALTH_CENTRAL with  grant  option;



drop table NEWR_REPOSB.PARTICIPANT_GAA_FUND_BALANCE;
CREATE TABLE NEWR_REPOSB.PARTICIPANT_GAA_FUND_BALANCE 
(
  CLIENT_ID VARCHAR2(10 BYTE) NOT NULL 
, PLAN_NUMBER VARCHAR2(25 BYTE) NOT NULL
, PARTICIPANT_ID VARCHAR2(25 BYTE) NOT NULL 
, FUND_NUMBER VARCHAR2(15 BYTE) 
, PLAN_END_YEAR VARCHAR2(13 BYTE)
, PM_OLTPLN_ISSUE_STATE VARCHAR2(5 BYTE)
, CURRENT_GAA_CONTRACT_AMOUNT NUMBER(17, 2) 
, ALL_CURR_GAA_ADJUSTED_AMOUNT NUMBER(17, 2) 
, ALL_CURR_GAA_ADJ_SURRENDER_AMT NUMBER(17, 2) 
, ALL_CURRENT_GAA_MVA_AMOUNT NUMBER(17, 2) 
, SURRENDER_PENALTY_AMT NUMBER(17, 2) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, SOURCE_CYCLE_DATE DATE ,
CONSTRAINT PK_PARTICIPANT_GAA_FUND_BAL PRIMARY KEY 
(
  CLIENT_ID 
, PARTICIPANT_ID 
, PLAN_NUMBER 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;

-- TABLE: NEWR_REPOSB.participant_gaa_fund_balance
--

GRANT SELECT ON NEWR_REPOSB.participant_gaa_fund_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_gaa_fund_balance TO role_newr_repos_write;

drop table NEWR_REPOSB.PARTICIPANT_GAA_FUND_BALANCE_DELTA;
CREATE TABLE NEWR_REPOSB.PARTICIPANT_GAA_FUND_BALANCE_DELTA 
(
  CLIENT_ID VARCHAR2(10 BYTE) NOT NULL 
, PLAN_NUMBER VARCHAR2(25 BYTE) NOT NULL
, PARTICIPANT_ID VARCHAR2(25 BYTE) NOT NULL 
, FUND_NUMBER VARCHAR2(15 BYTE) 
, PLAN_END_YEAR VARCHAR2(13 BYTE)
, PM_OLTPLN_ISSUE_STATE VARCHAR2(5 BYTE)
, CURRENT_GAA_CONTRACT_AMOUNT NUMBER(17, 2) 
, ALL_CURR_GAA_ADJUSTED_AMOUNT NUMBER(17, 2) 
, ALL_CURR_GAA_ADJ_SURRENDER_AMT NUMBER(17, 2) 
, ALL_CURRENT_GAA_MVA_AMOUNT NUMBER(17, 2) 
, SURRENDER_PENALTY_AMT NUMBER(17, 2) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, SOURCE_CYCLE_DATE DATE ,
DELTA_OP_IND varchar2(1)
)
TABLESPACE NEWR_REPOS_DATA
;

-- TABLE: NEWR_REPOSB.participant_gaa_fund_balance
--

GRANT SELECT ON NEWR_REPOSB.participant_gaa_fund_balance_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_gaa_fund_balance_delta TO role_newr_repos_write;

grant  SELECT on NEWR_REPOSB.participant_gaa_fund_balance to WEALTH_CENTRAL with  grant  option;


--participant_fund_balance

drop table NEWR_REPOSB.PARTICIPANT_FUND_BALANCE; 
CREATE TABLE NEWR_REPOSB.PARTICIPANT_FUND_BALANCE 
(
plan_number VARCHAR(25) ,
participant_id VARCHAR(25) ,
fund_number VARCHAR(15) ,
fund_iv VARCHAR(10) ,
cash_value_amount DECIMAL(17,2) ,
total_units DECIMAL(17,4) ,
ee_cash_value_amount DECIMAL(17,2) ,
er_cash_value_amount DECIMAL(17,2) ,
ytd_contributions DECIMAL(17,2) ,
source_cycle_date DATE,
CONSTRAINT PK_PARTICIPANT_FUND_BALANCE PRIMARY KEY 
(
  PARTICIPANT_ID 
, PLAN_NUMBER 
, FUND_NUMBER 
, SOURCE_CYCLE_DATE 
, FUND_IV 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;




-- TABLE: NEWR_REPOSB.participant_fund_balance_DELTA
--

GRANT SELECT ON NEWR_REPOSB.participant_fund_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_fund_balance TO role_newr_repos_write;

drop table NEWR_REPOSB.participant_fund_balance_DELTA;
cREATE TABLE NEWR_REPOSB.participant_fund_balance_DELTA
(
plan_number VARCHAR(25) ,
participant_id VARCHAR(25) ,
fund_number VARCHAR(15) ,
fund_iv VARCHAR(10) ,
cash_value_amount DECIMAL(17,2) ,
total_units DECIMAL(17,4) ,
ee_cash_value_amount DECIMAL(17,2) ,
er_cash_value_amount DECIMAL(17,2) ,
ytd_contributions DECIMAL(17,2) ,
source_cycle_date DATE,
DELTA_OP_IND varchar2(1)
)
TABLESPACE NEWR_REPOS_DATA
;




-- TABLE: NEWR_REPOSB.participant_fund_balance
--

GRANT SELECT ON NEWR_REPOSB.participant_fund_balance_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOSB.participant_fund_balance_DELTA TO role_newr_repos_write;


grant  SELECT on NEWR_REPOSB.participant_fund_balance to WEALTH_CENTRAL with  grant  option;
