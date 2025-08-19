from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.remote(cluster_id="0804-185424-c0xuuw82").getOrCreate()

spark.sql("SELECT 1").show()