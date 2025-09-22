from mlflow.tracking import MlflowClient

def main():
    client = MlflowClient()

    # List all registered models
    models = client.search_registered_models()
    print("Registered models:")
    for model in models:
        print(f"- {model.name}")

    # List versions of a specific model
    model_name = "workspace.default.fraud_detection_pipeline_model"
    try:
        versions = client.search_model_versions(f"name='{model_name}'")
        print(f"\nVersions for model '{model_name}':")
        for v in versions:
            print(f"  Version: {v.version}, Stage: {v.current_stage}")
    except Exception as e:
        print(f"Error fetching versions for model '{model_name}': {e}")

if __name__ == "__main__":
    main()
