from mlflow.tracking import MlflowClient

client = MlflowClient()

# Current full model name (invalid if contains dots, slashes, colons)
current_model_name = "workspace.default.fraud_detection_pipeline_model"

# New valid model name without forbidden characters
new_model_name = "fraud_detection_pipeline_model"

# Rename the model
client.rename_registered_model(current_model_name, new_model_name)

print(f"Model renamed from '{current_model_name}' to '{new_model_name}'")
