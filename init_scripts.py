# Databricks notebook source
dbutils.fs.mkdirs("dbfs:/databricks/script-test/")

# COMMAND ----------

dbutils.fs.put("/databricks/script-test/paramiko-install.sh","""
#!/bin/bash
/databricks/python/bin/pip uninstall pyOpenSSL -y
/databricks/python/bin/pip install pyOpenSSL==19.0.0
/databricks/python/bin/pip install cffi==1.8.2
/databricks/python/bin/pip install paramiko
""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/script-test/paramiko-install.sh"))
