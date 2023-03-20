# Databricks notebook source
words = sc.parallelize (["bish", "bash"])



# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG samples;
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG hive_metastore;
# MAGIC 
# MAGIC CREATE OR REPLACE TABLE sales_4312 (id INT, product STRING, salesAmt DECIMAL(12,2), unitsSold INT)
# MAGIC     COMMENT 'this is a comment'
# MAGIC     TBLPROPERTIES ('foo'='bar');

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sales_4312 (product, salesAmt, unitsSold) 
# MAGIC   VALUES ('test', 2.0, 1)
