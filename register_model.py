import mlflow

model_path = "./my_model"
model_name = "fraud_detection_pipeline_model"  # valid name without dots or slashes

# Register the model
mlflow.register_model(f"file://{model_path}", model_name)
