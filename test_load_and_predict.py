import mlflow
import pandas as pd

# Set the MLflow registry URI (same as your app)
mlflow.set_registry_uri("databricks-uc")

# The registered model URI, update as needed
model_uri = "models:/workspace.default.fraud_detection_pipeline_model@2"

def main():
    try:
        print(f"Loading model from: {model_uri}")
        model = mlflow.sklearn.load_model(model_uri)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Model loading failed: {e}")
        return

    # Prepare example input
    input_data = pd.DataFrame([{
        "TX_AMOUNT": 100.50,
        "TX_DURING_WEEKEND": 0,
        "TX_DURING_NIGHT": 1,
        "Cust_Nb_Tx_1Day": 5,
        "Cust_Avg_Amt_1Day": 50.75,
        "Cust_Nb_Tx_7Day": 30,
        "Cust_Avg_Amt_7Day": 48.20,
        "Cust_Nb_Tx_30Day": 120,
        "Cust_Avg_Amt_30Day": 47.00,
        "Term_Nb_Tx_1Day": 3,
        "Term_Risk_1Day": 0,
        "Term_Nb_Tx_7Day": 15,
        "Term_Risk_7Day": 0,
        "Term_Nb_Tx_30Day": 65,
        "Term_Risk_30Day": 1
    }])

    try:
        print("Running prediction...")
        preds = model.predict(input_data)
        print(f"Prediction result: {preds}")
    except Exception as e:
        print(f"Prediction failed: {e}")

if __name__ == "__main__":
    main()
