ALTER TABLE newr_repos.TRANSACTION_BALANCE_SUMMARY
drop CONSTRAINT PK_TRANSACTION_BALANCE_SUMMARY;

ALTER TABLE newr_repos.TRANSACTION_BALANCE_SUMMARY
ADD CONSTRAINT PK_TRANSACTION_BALANCE_SUMMARY PRIMARY KEY 
(
  CLIENT_ID 
, DIV_SUB_ID 
, FUND_ID 
, PLAN_NUMBER ,source_cycle_date
)using index tablespace NEWR_REPOS_INDEX;

ALTER TABLE newr_reposb.TRANSACTION_BALANCE_SUMMARY
drop CONSTRAINT PK_TRANSACTION_BALANCE_SUMMARY;

ALTER TABLE newr_reposb.TRANSACTION_BALANCE_SUMMARY
ADD CONSTRAINT PK_TRANSACTION_BALANCE_SUMMARY PRIMARY KEY 
(
  CLIENT_ID 
, DIV_SUB_ID 
, FUND_ID 
, PLAN_NUMBER ,source_cycle_date
)using index tablespace NEWR_REPOS_INDEX;