from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mlflow.sklearn
import pandas as pd


# Initialize FastAPI app
app = FastAPI()


# Define the input data schema
class TransactionFeatures(BaseModel):
    TX_AMOUNT: float
    TX_DURING_WEEKEND: int
    TX_DURING_NIGHT: int
    Cust_Nb_Tx_1Day: int
    Cust_Avg_Amt_1Day: float
    Cust_Nb_Tx_7Day: int
    Cust_Avg_Amt_7Day: float
    Cust_Nb_Tx_30Day: int
    Cust_Avg_Amt_30Day: float
    Term_Nb_Tx_1Day: int
    Term_Risk_1Day: int
    Term_Nb_Tx_7Day: int
    Term_Risk_7Day: int
    Term_Nb_Tx_30Day: int
    Term_Risk_30Day: int


# Load model at startup, use relative path or HF model registry URI
# It's recommended to avoid setting mlflow.set_tracking_uri inside app.py due to container environment constraints
# Instead, ensure MLflow tracking server info is managed externally (via env variable or secrets)
model_uri = "models:/workspace.default.fraud_detection_pipeline_model/2"

try:
    model = mlflow.sklearn.load_model(model_uri)
except Exception as e:
    # Logging could be enhanced here if using Python logging
    print(f"Model loading failed: {e}")
    model = None


@app.post("/predict/")
def predict(transactions: List[TransactionFeatures]):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    input_df = pd.DataFrame([t.dict() for t in transactions])
    try:
        predictions = model.predict(input_df)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
