import requests

# My Hugging Face Space URL
url = "https://dglassbrenner.hf.space/gradio_api"

# Make POST request to /predict/ endpoint
endpoint = url + "/predict/"

# Example JSON data matching TransactionFeatures schema (a list of transactions)
data = [
    {
        "TX_AMOUNT": 100.0,
        "TX_DURING_WEEKEND": 0,
        "TX_DURING_NIGHT": 1,
        "Cust_Nb_Tx_1Day": 5,
        "Cust_Avg_Amt_1Day": 50.0,
        "Cust_Nb_Tx_7Day": 30,
        "Cust_Avg_Amt_7Day": 60.0,
        "Cust_Nb_Tx_30Day": 120,
        "Cust_Avg_Amt_30Day": 65.0,
        "Term_Nb_Tx_1Day": 2,
        "Term_Risk_1Day": 0,
        "Term_Nb_Tx_7Day": 15,
        "Term_Risk_7Day": 0,
        "Term_Nb_Tx_30Day": 45,
        "Term_Risk_30Day": 1
    }
]

# Send the POST request
response = requests.post(endpoint, json=data)


print("Status code:", response.status_code)
print("Response JSON:", response.json())
