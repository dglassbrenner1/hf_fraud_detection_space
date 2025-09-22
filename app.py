import streamlit as st
import mlflow.sklearn
import pandas as pd

# Load model once (update model_uri accordingly)
model_uri = "./my_model" #"models:/workspace.default.fraud_detection_pipeline_model/1"
model = mlflow.sklearn.load_model(model_uri)

st.title("Fraud Detection Model Interface")
st.write("Enter transaction details below to get a fraud prediction:")

# Input fields matching your TransactionFeatures schema
TX_AMOUNT = st.number_input("Transaction Amount", min_value=0.0)
TX_DURING_WEEKEND = st.selectbox("Transaction During Weekend?", [0, 1])
TX_DURING_NIGHT = st.selectbox("Transaction During Night?", [0, 1])
Cust_Nb_Tx_1Day = st.number_input("Customer Number of Transactions in Last 1 Day", min_value=0)
Cust_Avg_Amt_1Day = st.number_input("Customer Avg Amount Last 1 Day", min_value=0.0)
Cust_Nb_Tx_7Day = st.number_input("Customer Number of Transactions in Last 7 Days", min_value=0)
Cust_Avg_Amt_7Day = st.number_input("Customer Avg Amount Last 7 Days", min_value=0.0)
Cust_Nb_Tx_30Day = st.number_input("Customer Number of Transactions in Last 30 Days", min_value=0)
Cust_Avg_Amt_30Day = st.number_input("Customer Avg Amount Last 30 Days", min_value=0.0)
Term_Nb_Tx_1Day = st.number_input("Terminal Number of Transactions in Last 1 Day", min_value=0)
Term_Risk_1Day = st.number_input("Terminal Risk Level Last 1 Day", min_value=0)
Term_Nb_Tx_7Day = st.number_input("Terminal Number of Transactions in Last 7 Days", min_value=0)
Term_Risk_7Day = st.number_input("Terminal Risk Level Last 7 Days", min_value=0)
Term_Nb_Tx_30Day = st.number_input("Terminal Number of Transactions in Last 30 Days", min_value=0)
Term_Risk_30Day = st.number_input("Terminal Risk Level Last 30 Days", min_value=0)

if st.button("Predict Fraud"):
    input_dict = {
        "TX_AMOUNT": TX_AMOUNT,
        "TX_DURING_WEEKEND": TX_DURING_WEEKEND,
        "TX_DURING_NIGHT": TX_DURING_NIGHT,
        "Cust_Nb_Tx_1Day": Cust_Nb_Tx_1Day,
        "Cust_Avg_Amt_1Day": Cust_Avg_Amt_1Day,
        "Cust_Nb_Tx_7Day": Cust_Nb_Tx_7Day,
        "Cust_Avg_Amt_7Day": Cust_Avg_Amt_7Day,
        "Cust_Nb_Tx_30Day": Cust_Nb_Tx_30Day,
        "Cust_Avg_Amt_30Day": Cust_Avg_Amt_30Day,
        "Term_Nb_Tx_1Day": Term_Nb_Tx_1Day,
        "Term_Risk_1Day": Term_Risk_1Day,
        "Term_Nb_Tx_7Day": Term_Nb_Tx_7Day,
        "Term_Risk_7Day": Term_Risk_7Day,
        "Term_Nb_Tx_30Day": Term_Nb_Tx_30Day,
        "Term_Risk_30Day": Term_Risk_30Day,
    }
    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0, 1]  # Probability of class 1 (fraud)

    # st.success(f"Fraud Prediction: {'Fraudulent' if prediction == 1 else 'Legitimate'}")
    st.write(f"Probability of fraud: {proba:.2%}")
