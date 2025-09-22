import mlflow

# Configure MLflow to use Databricks model registry
mlflow.set_registry_uri("databricks-uc")

# Now load your model with the correct registered model name
model = mlflow.pyfunc.load_model("models:/workspace.default.fraud_detection_pipeline_model/Production")
