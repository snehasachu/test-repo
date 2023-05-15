# Databricks notebook source
import requests
import json
# Replace with your Databricks instance hostname and access token
host = 'adb-5468803723918345.5.azuredatabricks.net'
token = ''
# Construct the API endpoint URL
url = f'https://{host}/api/2.0/clusters/create'
# Construct the request headers
headers = {
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}
# Construct the request payload
'''payload = {
    "cluster_name": "high-concurrency-cluster",
    "spark_version": "7.3.x-scala2.12",
    "node_type_id": "Standard_D3_v2",
    "spark_conf":{
          "spark.databricks.cluster.profile":"serverless",
          "spark.databricks.repl.allowedLanguages":"sql,python,r"
       },
     "custom_tags":{
          "ResourceClass":"Serverless"
       },
         "autoscale":{
          "min_workers":1,
          "max_workers":2
       },
    "autotermination_minutes":10
  }'''
payload = {
 'cluster_name': 'my-cluster',
  'spark_version': '7.3.x-scala2.12',
'node_type_id': 'Standard_D3_v2',
 'autoscale': {
  'min_workers': 2,
  'max_workers': 10
 }
}
# Send the HTTP request and handle the response
response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
  cluster = json.loads(response.content)
  print(f'Cluster created: {cluster["cluster_id"]}')
else:
  print(f'Error creating cluster: {response.content}')
