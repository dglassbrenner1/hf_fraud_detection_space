from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mlflow.sklearn
import pandas as pd
import mlflow
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set MLflow registry URI to Databricks Unity Catalog Model Registry
mlflow.set_registry_uri("databricks-uc")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

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


# Load model at startup; maybe @version or /version?
model_uri = "models:/workspace.default.fraud_detection_pipeline_model/1"
try:
    logger.info(f"Loading model from: {model_uri}")
    model = mlflow.sklearn.load_model(model_uri)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Model loading failed: {e}")
    model = None

@app.post("/predict/")
def predict(transactions: List[TransactionFeatures]):
    if model is None:
        logger.error("Attempted to predict but model is not loaded")
        raise HTTPException(status_code=503, detail="Model not loaded")

    input_df = pd.DataFrame([t.dict() for t in transactions])
    try:
        logger.info(f"Running prediction on input data: {input_df}")
        predictions = model.predict(input_df)
        logger.info(f"Prediction result: {predictions}")
        return {"predictions": predictions.tolist()}
    except Exception as e:
        logger.error(f"Inference failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

