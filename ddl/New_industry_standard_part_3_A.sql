
drop table NEWR_REPOS.PARTICIPANT_BALANCE;
drop table NEWR_REPOS.PARTICIPANT_BALANCE_delta;
drop table NEWR_REPOS.PARTICIPANT_BALANCE_monthly;
drop table NEWR_REPOS.PARTICIPANT_BALANCE_monthly_delta;
drop table NEWR_REPOS.PARTICIPANT_BALANCE_quarterly;
drop table NEWR_REPOS.PARTICIPANT_BALANCE_quarterly_delta;


-- participant_balance
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE TO role_newr_repos_write;




-- PARTICIPANT_BALANCE_monthly
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE_monthly 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE_monthly TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE_monthly TO role_newr_repos_write;


-- PARTICIPANT_BALANCE_quarterly
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE_quarterly 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE_quarterly TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE_quarterly TO role_newr_repos_write;



-- participant_balance_delta
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE_delta 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE_delta TO role_newr_repos_write;




-- PARTICIPANT_BALANCE_monthly_delta
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE_monthly_delta 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE_monthly_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE_monthly_delta TO role_newr_repos_write;


-- PARTICIPANT_BALANCE_quarterly_delta
CREATE TABLE NEWR_REPOS.PARTICIPANT_BALANCE_quarterly_delta 
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
GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BALANCE_quarterly_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BALANCE_quarterly_delta TO role_newr_repos_write;


grant  SELECT on NEWR_REPOS.PARTICIPANT_BALANCE_quarterly to WEALTH_CENTRAL with  grant  option;
grant  SELECT on NEWR_REPOS.PARTICIPANT_BALANCE_monthly to WEALTH_CENTRAL with  grant  option;
grant  SELECT on NEWR_REPOS.participant_balance to WEALTH_CENTRAL with  grant  option;

drop table NEWR_REPOS.TABLE PART_SOURCE_TRANSFER_BALANCE;
drop table NEWR_REPOS.TABLE PART_SOURCE_TRANSFER_BALANCE_delta;
--part_source_transfer_balance

CREATE TABLE NEWR_REPOS.PARTICIPANT_SOURCE_TRANSFER_BALANCE 
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

CREATE TABLE NEWR_REPOS.PARTICIPANT_SOURCE_TRANSFER_BALANCE_DELTA 
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

-- TABLE: NEWR_REPOS.part_source_transfer_balance
--

GRANT SELECT ON NEWR_REPOS.participant_source_transfer_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_source_transfer_balance TO role_newr_repos_write;

-- TABLE: NEWR_REPOS.part_source_transfer_balance
--

GRANT SELECT ON NEWR_REPOS.participant_source_transfer_balance_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_source_transfer_balance_DELTA TO role_newr_repos_write;


grant  SELECT on NEWR_REPOS.participant_source_transfer_balance to WEALTH_CENTRAL with  grant  option;


drop table NEWR_REPOS.SOURCE_FUND_FUTURE_ALLOCATION;
CREATE TABLE NEWR_REPOS.SOURCE_FUND_FUTURE_ALLOCATION 
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
 

-- TABLE: NEWR_REPOS.source_fund_future_allocation
--

GRANT SELECT ON NEWR_REPOS.source_fund_future_allocation TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.source_fund_future_allocation TO role_newr_repos_write;

drop table NEWR_REPOS.SOURCE_FUND_FUTURE_ALLOCATION_DELTA;
CREATE TABLE NEWR_REPOS.SOURCE_FUND_FUTURE_ALLOCATION_DELTA 
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
 

-- TABLE: NEWR_REPOS.source_fund_future_allocation
--

GRANT SELECT ON NEWR_REPOS.source_fund_future_allocation_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.source_fund_future_allocation_delta TO role_newr_repos_write;

grant  SELECT on NEWR_REPOS.source_fund_future_allocation to WEALTH_CENTRAL with  grant  option;

drop table NEWR_REPOS.PARTICIPANT_GAA_FUND_BALANCE;
CREATE TABLE NEWR_REPOS.PARTICIPANT_GAA_FUND_BALANCE 
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

-- TABLE: NEWR_REPOS.participant_gaa_fund_balance
--

GRANT SELECT ON NEWR_REPOS.participant_gaa_fund_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_gaa_fund_balance TO role_newr_repos_write;

drop table NEWR_REPOS.PARTICIPANT_GAA_FUND_BALANCE_DELTA;
CREATE TABLE NEWR_REPOS.PARTICIPANT_GAA_FUND_BALANCE_DELTA 
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

-- TABLE: NEWR_REPOS.participant_gaa_fund_balance
--

GRANT SELECT ON NEWR_REPOS.participant_gaa_fund_balance_delta TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_gaa_fund_balance_delta TO role_newr_repos_write;

grant  SELECT on NEWR_REPOS.participant_gaa_fund_balance to WEALTH_CENTRAL with  grant  option;


--participant_fund_balance

drop table NEWR_REPOS.PARTICIPANT_FUND_BALANCE; 
CREATE TABLE NEWR_REPOS.PARTICIPANT_FUND_BALANCE 
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




-- TABLE: NEWR_REPOS.participant_fund_balance_DELTA
--

GRANT SELECT ON NEWR_REPOS.participant_fund_balance TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_fund_balance TO role_newr_repos_write;

drop table NEWR_REPOS.participant_fund_balance_DELTA;
cREATE TABLE NEWR_REPOS.participant_fund_balance_DELTA
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




-- TABLE: NEWR_REPOS.participant_fund_balance
--

GRANT SELECT ON NEWR_REPOS.participant_fund_balance_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.participant_fund_balance_DELTA TO role_newr_repos_write;


grant  SELECT on NEWR_REPOS.participant_fund_balance to WEALTH_CENTRAL with  grant  option;



--participant_source

DROP TABLE NEWR_REPOS.PARTICIPANT_SOURCE;

CREATE TABLE NEWR_REPOS.PARTICIPANT_SOURCE 
(
  CLIENT_ID VARCHAR2(10 BYTE) 
, PLAN_NUMBER VARCHAR2(25 BYTE)
, PARTICIPANT_ID VARCHAR2(25 BYTE) 
, MONEY_SOURCE VARCHAR2(10 BYTE) 
, MONEY_SOURCE_NAME VARCHAR2(30 BYTE) 
, FIRST_CONTRIBUTION_DATE DATE 
, FIRST_ROTH_CONTRIBUTION_DATE DATE 
, ELECTED_CONTRIBUTION_AMOUNT NUMBER(13, 2) 
, ELECTED_CONTRIBUTION_PERCENT NUMBER(13, 2) 
, FUTURE_CATCHUP_DEF_PCT NUMBER(9, 6) 
, NEXT_SCHEDULED_INCREASE_DATE DATE 
, ONE_TIME_DEFERRAL_PERCENT NUMBER(9, 6) 
, PRIOR_DEFERRAL_AMOUNT NUMBER(13, 2) 
, PRIOR_DEFERRAL_RATE NUMBER(13, 2) 
, EE_DEFERRAL_RATE_ELECT NUMBER(9, 6) 
, RATE_ESCALATOR_CREATION_DATE DATE 
, RATE_ESCALATOR_DOLLAR_AMOUNT NUMBER(7, 2) 
, SUPPLEMENTAL_DEERRAL_DOLLAR_PRIOR NUMBER(13, 2) 
, RATE_ESCALATOR_FREQUENCY VARCHAR2(1 BYTE) 
, RATE_ESCALATOR_INC_PERCENT NUMBER(7, 2) 
, RATE_ESCALATOR_MAX_PERCENT NUMBER(7, 2) 
, SOURCE_ADJ_VEST_PERCENT NUMBER(6, 3) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, ACTUAL_CONTRIBUTION_AMOUNT NUMBER(13, 2) 
, ACTUAL_CONTRIBUTION_PERCENT NUMBER(13, 2) 
, ACTUAL_DEFERRAL_AMOUNT NUMBER(11, 2) 
, CATCHUP_DEFERRAL_AMOUNT NUMBER(11, 2) 
, CATCHUP_FUTURE_DEFERRAL_AMOUNT NUMBER(11, 2) 
, DEFERRAL_DOLLAR_AMOUNT_ELECTED NUMBER(11, 2) 
, DEFERRAL_SELECTION VARCHAR2(1 BYTE) 
, EE_CATCHUP_DEFERRAL_PERCENT NUMBER(9, 6) 
, DEFERRAL_RATE_ACTUAL VARCHAR2(20 BYTE) ,
CONSTRAINT PK_PARTICIPANT_SOURCE PRIMARY KEY 
(
  CLIENT_ID 
, PARTICIPANT_ID 
, PLAN_NUMBER 
, MONEY_SOURCE 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PARTICIPANT_SOURCE TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_SOURCE TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PARTICIPANT_SOURCE TO WEALTH_CENTRAL WITH  GRANT  OPTION;

--

--
DROP TABLE NEWR_REPOS.PARTICIPANT_SOURCE_DELTA;

CREATE TABLE NEWR_REPOS.PARTICIPANT_SOURCE_DELTA
(
  CLIENT_ID VARCHAR2(10 BYTE) 
, PLAN_NUMBER VARCHAR2(25 BYTE)
, PARTICIPANT_ID VARCHAR2(25 BYTE) 
, MONEY_SOURCE VARCHAR2(10 BYTE) 
, MONEY_SOURCE_NAME VARCHAR2(30 BYTE) 
, FIRST_CONTRIBUTION_DATE DATE 
, FIRST_ROTH_CONTRIBUTION_DATE DATE 
, ELECTED_CONTRIBUTION_AMOUNT NUMBER(13, 2) 
, ELECTED_CONTRIBUTION_PERCENT NUMBER(13, 2) 
, FUTURE_CATCHUP_DEF_PCT NUMBER(9, 6) 
, NEXT_SCHEDULED_INCREASE_DATE DATE 
, ONE_TIME_DEFERRAL_PERCENT NUMBER(9, 6) 
, PRIOR_DEFERRAL_AMOUNT NUMBER(13, 2) 
, PRIOR_DEFERRAL_RATE NUMBER(13, 2) 
, EE_DEFERRAL_RATE_ELECT NUMBER(9, 6) 
, RATE_ESCALATOR_CREATION_DATE DATE 
, RATE_ESCALATOR_DOLLAR_AMOUNT NUMBER(7, 2) 
, SUPPLEMENTAL_DEERRAL_DOLLAR_PRIOR NUMBER(13, 2) 
, RATE_ESCALATOR_FREQUENCY VARCHAR2(1 BYTE) 
, RATE_ESCALATOR_INC_PERCENT NUMBER(7, 2) 
, RATE_ESCALATOR_MAX_PERCENT NUMBER(7, 2) 
, SOURCE_ADJ_VEST_PERCENT NUMBER(6, 3) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, ACTUAL_CONTRIBUTION_AMOUNT NUMBER(13, 2) 
, ACTUAL_CONTRIBUTION_PERCENT NUMBER(13, 2) 
, ACTUAL_DEFERRAL_AMOUNT NUMBER(11, 2) 
, CATCHUP_DEFERRAL_AMOUNT NUMBER(11, 2) 
, CATCHUP_FUTURE_DEFERRAL_AMOUNT NUMBER(11, 2) 
, DEFERRAL_DOLLAR_AMOUNT_ELECTED NUMBER(11, 2) 
, DEFERRAL_SELECTION VARCHAR2(1 BYTE) 
, EE_CATCHUP_DEFERRAL_PERCENT NUMBER(9, 6) 
, DEFERRAL_RATE_ACTUAL VARCHAR2(20 BYTE)
, DELTA_OP_IND VARCHAR2(1 BYTE),
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PARTICIPANT_SOURCE_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_SOURCE_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PARTICIPANT_SOURCE_DELTA TO WEALTH_CENTRAL WITH  GRANT  OPTION;



--plan_fund

DROP TABLE NEWR_REPOS.PLAN_FUND;

CREATE TABLE NEWR_REPOS.PLAN_FUND 
(
  CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)    
, DIV_SUB_ID VARCHAR2(10 BYTE) 
, FUND_IV VARCHAR2(10 BYTE) 
, FUND_NUMBER VARCHAR2(15 BYTE) 
, FUND_NAME VARCHAR2(100 BYTE) 
, FUND_ABBR_NAME VARCHAR2(8 BYTE)
, SHARES VARCHAR2(1 BYTE) 
, SHARE_PRICE NUMBER(11, 6)
, TICKER_SYMBOL VARCHAR2(15 BYTE)
, FUND_FAMILY_ABBR_NAME VARCHAR2(8 BYTE)
, FUND_SEPARATE_ACCOUNT VARCHAR2(30 BYTE) 
, ASSET_CODE VARCHAR2(50 BYTE) 
, ASSET_NAME VARCHAR2(35 BYTE) 
, ASSET_CLASS_DESC CLOB 
, FUND_INCEPTION_DATE DATE 
, FUND_INCEPTION_INDICATOR VARCHAR2(10 BYTE) 
, FIXED_FUND_INDICATOR VARCHAR2(10 BYTE) 
, FIXED_TYP VARCHAR2(10 BYTE) 
, STMT_ASSET_CLASS VARCHAR2(8 BYTE) 
, ACC_FUND_INDICATOR VARCHAR2(10 BYTE) 
, STK_INDICATOR VARCHAR2(10 BYTE) 
, ACCOUNTING_METHOD_INDICATOR VARCHAR2(10 BYTE) 
, STABI_FUND_INVEST_CONTRACT_NUM VARCHAR2(12 BYTE)  
, ADM_FEE_D_FCT NUMBER(13, 4) 
, ADM_FEE_RATE NUMBER(13, 4) 
, ADM_FUND_NUM VARCHAR2(10 BYTE) 
, ADVR_FEE_D_FCT NUMBER(13, 4) 
, AUTO_ENROLL_INDICATOR VARCHAR2(10 BYTE) 
, AUTO_ENROLL_DATE DATE 
, DIV_PAYFREQ_CD VARCHAR2(10 BYTE) 
, DIVIDEND_PASS_THRU_OPTION VARCHAR2(10 BYTE) 
, DIVIDEND_RATE NUMBER(13, 10) 
, DIVIDEND_RECORD_DATE DATE  
, DIVIDEND_REINVEST_DATE DATE 
, DEFAULT_DEFERRAL_AMOUNT NUMBER(11, 6) 
, DEFAULT_DEFERRAL_PERCENT NUMBER(11, 6) 
, DEFAULT_INVEST_ELECTION_PCT NUMBER(11, 6) 
, FUND_INDEX_ID VARCHAR2(10 BYTE) 
, FUND_PERF_INDICATOR VARCHAR2(10 BYTE)
, FUND_RISK_RTN NUMBER(19, 0) 
, GROUP_FUND_INDICATOR VARCHAR2(10 BYTE) 
, INVST_STYLE VARCHAR2(30 BYTE) 
, INVESTMENT_MANAGER_ID VARCHAR2(20 BYTE) 
, INVESTMENT_ASSET_TYPE VARCHAR2(10 BYTE) 
, INVESTMENT_TYPE VARCHAR2(20 BYTE) 
, INVESTMENT_NAME_LONG_VERSION VARCHAR2(100 BYTE) 
, MID_FUND_NAME VARCHAR2(255 BYTE) 
, MKTG_FUND_NUMBER VARCHAR2(10 BYTE) 
, OUTSD_FUND_NUM VARCHAR2(10 BYTE)  
, PRICE_ID VARCHAR2(15 BYTE) 
, M_D_DIV_AMT_HI NUMBER(13, 4) 
, M_D_DIV_AMT_LO NUMBER(13, 4) 
, M_D_DIV_DAY VARCHAR2(10 BYTE) 
, S_D_DIV_AMT_HI NUMBER(13, 4) 
, S_D_DIV_AMT_LO NUMBER(13, 4) 
, SADV_FEE_D_FCT NUMBER(13, 4) 
, SADV_FEE_RATE NUMBER(13, 4) 
, SHARE_PRICE_INDICATOR VARCHAR2(10 BYTE) 
, TRUST_NUMBER VARCHAR2(6 BYTE) 
, TRD_INST_FFAM VARCHAR2(40 BYTE)
, SINGLE_SHARE_VALUE NUMBER(11, 6) 
, FRACTIONAL_SHARE_IND NUMBER(38, 0)
, EQUIVALENT_SHARES_FACTOR VARCHAR2(10 BYTE) 
, ADVR_FEE_RATE NUMBER(13, 4) 
, FUND_ADJ_PRICE_INDICATOR VARCHAR2(10 BYTE) 
, FUND_AET_SER_P_INDICATOR VARCHAR2(10 BYTE) 
, FUND_AVAIL_PROD DATE 
, PROPORTIONAL_PERCENTAGE NUMBER(3, 2)
, PRT_FEE_FCT NUMBER(13, 4) 
, PRT_FEE_RATE NUMBER(13, 4) 
, QUALIFIED_STOCK_FUND_INDICATOR VARCHAR2(10 BYTE) 
, YB04_D_FCT NUMBER(13, 4) 
, YB04_RATE NUMBER(5, 2) 
, AUV_MOVE_DATE DATE 
, AT_FILE_IND VARCHAR2(254 BYTE) 
, EXPED_INDICATOR VARCHAR2(10 BYTE)
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, FUND_ID VARCHAR2(10 BYTE) ,
CONSTRAINT PK_PLAN_FUND PRIMARY KEY 
(
  CLIENT_ID 
, FUND_NUMBER 
, PLAN_NUMBER 
, FUND_IV 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PLAN_FUND TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_FUND TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_FUND TO WEALTH_CENTRAL WITH GRANT OPTION;


--
DROP TABLE NEWR_REPOS.PLAN_FUND_DELTA;

CREATE TABLE NEWR_REPOS.PLAN_FUND_DELTA
(
  CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)    
, DIV_SUB_ID VARCHAR2(10 BYTE) 
, FUND_IV VARCHAR2(10 BYTE) 
, FUND_NUMBER VARCHAR2(15 BYTE) 
, FUND_NAME VARCHAR2(100 BYTE) 
, FUND_ABBR_NAME VARCHAR2(8 BYTE)
, SHARES VARCHAR2(1 BYTE) 
, SHARE_PRICE NUMBER(11, 6)
, TICKER_SYMBOL VARCHAR2(15 BYTE)
, FUND_FAMILY_ABBR_NAME VARCHAR2(8 BYTE)
, FUND_SEPARATE_ACCOUNT VARCHAR2(30 BYTE) 
, ASSET_CODE VARCHAR2(50 BYTE) 
, ASSET_NAME VARCHAR2(35 BYTE) 
, ASSET_CLASS_DESC CLOB 
, FUND_INCEPTION_DATE DATE 
, FUND_INCEPTION_INDICATOR VARCHAR2(10 BYTE) 
, FIXED_FUND_INDICATOR VARCHAR2(10 BYTE) 
, FIXED_TYP VARCHAR2(10 BYTE) 
, STMT_ASSET_CLASS VARCHAR2(8 BYTE) 
, ACC_FUND_INDICATOR VARCHAR2(10 BYTE) 
, STK_INDICATOR VARCHAR2(10 BYTE) 
, ACCOUNTING_METHOD_INDICATOR VARCHAR2(10 BYTE) 
, STABI_FUND_INVEST_CONTRACT_NUM VARCHAR2(12 BYTE)  
, ADM_FEE_D_FCT NUMBER(13, 4) 
, ADM_FEE_RATE NUMBER(13, 4) 
, ADM_FUND_NUM VARCHAR2(10 BYTE) 
, ADVR_FEE_D_FCT NUMBER(13, 4) 
, AUTO_ENROLL_INDICATOR VARCHAR2(10 BYTE) 
, AUTO_ENROLL_DATE DATE 
, DIV_PAYFREQ_CD VARCHAR2(10 BYTE) 
, DIVIDEND_PASS_THRU_OPTION VARCHAR2(10 BYTE) 
, DIVIDEND_RATE NUMBER(13, 10) 
, DIVIDEND_RECORD_DATE DATE  
, DIVIDEND_REINVEST_DATE DATE 
, DEFAULT_DEFERRAL_AMOUNT NUMBER(11, 6) 
, DEFAULT_DEFERRAL_PERCENT NUMBER(11, 6) 
, DEFAULT_INVEST_ELECTION_PCT NUMBER(11, 6) 
, FUND_INDEX_ID VARCHAR2(10 BYTE) 
, FUND_PERF_INDICATOR VARCHAR2(10 BYTE)
, FUND_RISK_RTN NUMBER(19, 0) 
, GROUP_FUND_INDICATOR VARCHAR2(10 BYTE) 
, INVST_STYLE VARCHAR2(30 BYTE) 
, INVESTMENT_MANAGER_ID VARCHAR2(20 BYTE) 
, INVESTMENT_ASSET_TYPE VARCHAR2(10 BYTE) 
, INVESTMENT_TYPE VARCHAR2(20 BYTE) 
, INVESTMENT_NAME_LONG_VERSION VARCHAR2(100 BYTE) 
, MID_FUND_NAME VARCHAR2(255 BYTE) 
, MKTG_FUND_NUMBER VARCHAR2(10 BYTE) 
, OUTSD_FUND_NUM VARCHAR2(10 BYTE)  
, PRICE_ID VARCHAR2(15 BYTE) 
, M_D_DIV_AMT_HI NUMBER(13, 4) 
, M_D_DIV_AMT_LO NUMBER(13, 4) 
, M_D_DIV_DAY VARCHAR2(10 BYTE) 
, S_D_DIV_AMT_HI NUMBER(13, 4) 
, S_D_DIV_AMT_LO NUMBER(13, 4) 
, SADV_FEE_D_FCT NUMBER(13, 4) 
, SADV_FEE_RATE NUMBER(13, 4) 
, SHARE_PRICE_INDICATOR VARCHAR2(10 BYTE) 
, TRUST_NUMBER VARCHAR2(6 BYTE) 
, TRD_INST_FFAM VARCHAR2(40 BYTE)
, SINGLE_SHARE_VALUE NUMBER(11, 6) 
, FRACTIONAL_SHARE_IND NUMBER(38, 0)
, EQUIVALENT_SHARES_FACTOR VARCHAR2(10 BYTE) 
, ADVR_FEE_RATE NUMBER(13, 4) 
, FUND_ADJ_PRICE_INDICATOR VARCHAR2(10 BYTE) 
, FUND_AET_SER_P_INDICATOR VARCHAR2(10 BYTE) 
, FUND_AVAIL_PROD DATE 
, PROPORTIONAL_PERCENTAGE NUMBER(3, 2)
, PRT_FEE_FCT NUMBER(13, 4) 
, PRT_FEE_RATE NUMBER(13, 4) 
, QUALIFIED_STOCK_FUND_INDICATOR VARCHAR2(10 BYTE) 
, YB04_D_FCT NUMBER(13, 4) 
, YB04_RATE NUMBER(5, 2) 
, AUV_MOVE_DATE DATE 
, AT_FILE_IND VARCHAR2(254 BYTE) 
, EXPED_INDICATOR VARCHAR2(10 BYTE)
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, FUND_ID VARCHAR2(10 BYTE) 
, DELTA_OP_IND VARCHAR2(1 BYTE)
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PLAN_FUND_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_FUND_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_FUND_DELTA TO WEALTH_CENTRAL WITH GRANT OPTION;



--plan_source
DROP TABLE NEWR_REPOS.PLAN_SOURCE;

CREATE TABLE NEWR_REPOS.PLAN_SOURCE 
(
  CLIENT_ID VARCHAR2(10 BYTE) 
, PLAN_NUMBER VARCHAR2(25 BYTE) 
, MONEY_SOURCE VARCHAR2(20 BYTE) 
, MONEY_SOURCE_NAME_LONG VARCHAR2(100 BYTE) 
, ROTH_DEFERRAL_SOURCE_INDICATOR VARCHAR2(1 BYTE) 
, VESTING_METHOD VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE_LABEL VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE_PERCENT VARCHAR2(20 BYTE) 
, VESTING_SCHEDULE_PERIOD VARCHAR2(50 BYTE) 
, MONEY_TYPE_CODE VARCHAR2(2 BYTE) 
, MONEY_TYPE_NAME VARCHAR2(10 BYTE) 
, SOURCE_SYSTEM VARCHAR2(100 BYTE) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE ,
CONSTRAINT PK_PLAN_SOURCE PRIMARY KEY 
(
  CLIENT_ID 
, MONEY_SOURCE 
, PLAN_NUMBER 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;


GRANT SELECT ON NEWR_REPOS.PLAN_SOURCE TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_SOURCE TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_SOURCE TO WEALTH_CENTRAL WITH GRANT OPTION;



--
DROP TABLE NEWR_REPOS.PLAN_SOURCE_DELTA;

CREATE TABLE NEWR_REPOS.PLAN_SOURCE_DELTA
(
  CLIENT_ID VARCHAR2(10 BYTE) 
, PLAN_NUMBER VARCHAR2(25 BYTE) 
, MONEY_SOURCE VARCHAR2(20 BYTE) 
, MONEY_SOURCE_NAME_LONG VARCHAR2(100 BYTE) 
, ROTH_DEFERRAL_SOURCE_INDICATOR VARCHAR2(1 BYTE) 
, VESTING_METHOD VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE_LABEL VARCHAR2(50 BYTE) 
, VESTING_SCHEDULE_PERCENT VARCHAR2(20 BYTE) 
, VESTING_SCHEDULE_PERIOD VARCHAR2(50 BYTE) 
, MONEY_TYPE_CODE VARCHAR2(2 BYTE) 
, MONEY_TYPE_NAME VARCHAR2(10 BYTE) 
, SOURCE_SYSTEM VARCHAR2(100 BYTE) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, DELTA_OP_IND VARCHAR2( 1 BYTE)
)
TABLESPACE NEWR_REPOS_DATA
;


GRANT SELECT ON NEWR_REPOS.PLAN_SOURCE_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_SOURCE_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_SOURCE_DELTA TO WEALTH_CENTRAL WITH GRANT OPTION;



--plan_withdrawal_type

DROP TABLE NEWR_REPOS.PLAN_WITHDRAWAL_TYPE;

CREATE TABLE NEWR_REPOS.PLAN_WITHDRAWAL_TYPE 
(
  CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)
, WITHDRAWAL_TYPE VARCHAR2(254 BYTE)
, WITHDRAWAL_CODE VARCHAR2(254 BYTE)
, WITHDRAWAL_DESCRIPTION VARCHAR2(254 BYTE) 
, DISTRIBUTION_FEE NUMBER(11, 4) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE, 
CONSTRAINT PK_PLAN_WITHDRAWAL_TYPE PRIMARY KEY 
(
  CLIENT_ID 
, PLAN_NUMBER 
, WITHDRAWAL_CODE 
, WITHDRAWAL_TYPE 
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE TO WEALTH_CENTRAL WITH GRANT OPTION;





--

DROP TABLE NEWR_REPOS.PLAN_WITHDRAWAL_TYPE_DELTA;

CREATE TABLE NEWR_REPOS.PLAN_WITHDRAWAL_TYPE_DELTA
(
  CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)
, WITHDRAWAL_TYPE VARCHAR2(254 BYTE)
, WITHDRAWAL_CODE VARCHAR2(254 BYTE)
, WITHDRAWAL_DESCRIPTION VARCHAR2(254 BYTE) 
, DISTRIBUTION_FEE NUMBER(11, 4) 
, SOURCE_SYSTEM VARCHAR2(80 BYTE) 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE
, DELTA_OP_IND VARCHAR2(1 BYTE)
)
TABLESPACE NEWR_REPOS_DATA
;

GRANT SELECT ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PLAN_WITHDRAWAL_TYPE_DELTA TO WEALTH_CENTRAL WITH GRANT OPTION;



--participant_beneficiary

DROP TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY;

CREATE TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY 
(
 CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)
, PARTICIPANT_ID VARCHAR2(25 BYTE)
, BENEFICIARY_TIN VARCHAR2(20 BYTE)
, BENEFICIARY_TYPE VARCHAR2(10 BYTE)
, BENEFICIARY_NAME VARCHAR2(255 BYTE) 
, BENEFICIARY_STATUS VARCHAR2(50 BYTE) 
, RELATIONSHIP_ID VARCHAR2(10 BYTE) 
, RELATIONSHIP_NAME VARCHAR2(255 BYTE) 
, ADDRESS_LINE_1 VARCHAR2(255 BYTE) 
, CITY VARCHAR2(40 BYTE) 
, STATE VARCHAR2(100 BYTE) 
, ZIP_CODE VARCHAR2(50 BYTE) 
, PARTICIPANT_BENEFICIARY VARCHAR2(50 BYTE) 
, BENEFICIARY_LEVEL VARCHAR2(50 BYTE) 
, BENEFICIARY_PERCENT_TYPE VARCHAR2(50 BYTE) 
, BENEFICIARY_CATEGORY VARCHAR2(50 BYTE) 
, BENEFICIARY_ALLOCATION_PERCENT NUMBER(5, 2) 
, BENEFICIARY_LAST_CHANGE_DATE DATE 
, BIRTH_DATE DATE 
, GENDER VARCHAR2(50 BYTE) 
, FOREIGN_ADDRESS_INDICATOR VARCHAR2(50 BYTE) 
, PRIMARY_CONTINGENT_INDICATOR VARCHAR2(50 BYTE) 
, ORIGIN_CHANGED VARCHAR2(10 BYTE) 
, SIGNED_DATE DATE 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE)
, BENEFICIARY_SEQUENCE_NUMBER NUMBER(38, 0) ,
CONSTRAINT PK_PARTICIPANT_BENEFICIARY PRIMARY KEY 
(
  BENEFICIARY_TIN 
, CLIENT_ID 
, PARTICIPANT_ID 
, PLAN_NUMBER 
, BENEFICIARY_TYPE 
, BENEFICIARY_SEQUENCE_NUMBER
)
USING INDEX
TABLESPACE NEWR_REPOS_INDEX
)
TABLESPACE NEWR_REPOS_DATA
;


GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BENEFICIARY TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY TO WEALTH_CENTRAL WITH GRANT OPTION;




--
DROP TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA;

CREATE TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA
(
 CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)
, PARTICIPANT_ID VARCHAR2(25 BYTE)
, BENEFICIARY_TIN VARCHAR2(20 BYTE)
, BENEFICIARY_TYPE VARCHAR2(10 BYTE)
, BENEFICIARY_NAME VARCHAR2(255 BYTE) 
, BENEFICIARY_STATUS VARCHAR2(50 BYTE) 
, RELATIONSHIP_ID VARCHAR2(10 BYTE) 
, RELATIONSHIP_NAME VARCHAR2(255 BYTE) 
, ADDRESS_LINE_1 VARCHAR2(255 BYTE) 
, CITY VARCHAR2(40 BYTE) 
, STATE VARCHAR2(100 BYTE) 
, ZIP_CODE VARCHAR2(50 BYTE) 
, PARTICIPANT_BENEFICIARY VARCHAR2(50 BYTE) 
, BENEFICIARY_LEVEL VARCHAR2(50 BYTE) 
, BENEFICIARY_PERCENT_TYPE VARCHAR2(50 BYTE) 
, BENEFICIARY_CATEGORY VARCHAR2(50 BYTE) 
, BENEFICIARY_ALLOCATION_PERCENT NUMBER(5, 2) 
, BENEFICIARY_LAST_CHANGE_DATE DATE 
, BIRTH_DATE DATE 
, GENDER VARCHAR2(50 BYTE) 
, FOREIGN_ADDRESS_INDICATOR VARCHAR2(50 BYTE) 
, PRIMARY_CONTINGENT_INDICATOR VARCHAR2(50 BYTE) 
, ORIGIN_CHANGED VARCHAR2(10 BYTE) 
, SIGNED_DATE DATE 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE)
, BENEFICIARY_SEQUENCE_NUMBER NUMBER(38, 0)
, DELTA_OP_IND VARCHAR2(1)
)
TABLESPACE NEWR_REPOS_DATA
;


GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO WEALTH_CENTRAL WITH GRANT OPTION;


--
DROP TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA;

CREATE TABLE NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA 
(
 CLIENT_ID VARCHAR2(10 BYTE)
, PLAN_NUMBER VARCHAR2(25 BYTE)
, PARTICIPANT_ID VARCHAR2(25 BYTE)
, BENEFICIARY_TIN VARCHAR2(20 BYTE)
, BENEFICIARY_TYPE VARCHAR2(10 BYTE)
, BENEFICIARY_NAME VARCHAR2(255 BYTE) 
, BENEFICIARY_STATUS VARCHAR2(50 BYTE) 
, RELATIONSHIP_ID VARCHAR2(10 BYTE) 
, RELATIONSHIP_NAME VARCHAR2(255 BYTE) 
, ADDRESS_LINE_1 VARCHAR2(255 BYTE) 
, CITY VARCHAR2(40 BYTE) 
, STATE VARCHAR2(100 BYTE) 
, ZIP_CODE VARCHAR2(50 BYTE) 
, PARTICIPANT_BENEFICIARY VARCHAR2(50 BYTE) 
, BENEFICIARY_LEVEL VARCHAR2(50 BYTE) 
, BENEFICIARY_PERCENT_TYPE VARCHAR2(50 BYTE) 
, BENEFICIARY_CATEGORY VARCHAR2(50 BYTE) 
, BENEFICIARY_ALLOCATION_PERCENT NUMBER(5, 2) 
, BENEFICIARY_LAST_CHANGE_DATE DATE 
, BIRTH_DATE DATE 
, GENDER VARCHAR2(50 BYTE) 
, FOREIGN_ADDRESS_INDICATOR VARCHAR2(50 BYTE) 
, PRIMARY_CONTINGENT_INDICATOR VARCHAR2(50 BYTE) 
, ORIGIN_CHANGED VARCHAR2(10 BYTE) 
, SIGNED_DATE DATE 
, SOURCE_CYCLE_DATE DATE 
, SOURCE_PROCESSING_DATE DATE 
, SOURCE_SYSTEM VARCHAR2(80 BYTE)
, BENEFICIARY_SEQUENCE_NUMBER NUMBER(38, 0) 
, DELTA_OP_IND VARCHAR2(1)
)
TABLESPACE NEWR_REPOS_DATA
;


GRANT SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO role_newr_repos_read;
GRANT INSERT, UPDATE, DELETE ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO role_newr_repos_write;

GRANT  SELECT ON NEWR_REPOS.PARTICIPANT_BENEFICIARY_DELTA TO WEALTH_CENTRAL WITH GRANT OPTION;


