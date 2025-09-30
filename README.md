---
title: Fraud Detection Api
emoji: 🏢
colorFrom: red
colorTo: purple
sdk: docker
pinned: false
license: apache-2.0
short_description: A fraud detection api
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Fraud Detection API

This repository contains the code and resources for a **fraud detection model deployed as a Hugging Face Space** with a Streamlit API, powered by an XGBoost model trained and registered via MLflow in Databricks.

## Overview

The fraud detection solution provides a Streamlit app where users can input individual transaction features and get a prediction probability of the transaction being fraudulent. The app loads a tuned XGBoost pipeline model that was trained on historical transaction data.

### Features

- Deploys a fraud detection XGBoost model in Hugging Face Spaces.
- Streamlit-based interactive web API for individual transaction fraud prediction.
- Model registered and managed with MLflow in Databricks.
- Uses feature inputs such as transaction amount, time, customer and terminal transaction histories, and risk metrics.

### Hugging Face Space Link

Access the live app here:

[Fraud Detection Model Interface](https://huggingface.co/spaces/dglassbrenner/fraud_detection_api)

## Repository Structure

- `.github/workflows/sync_to_hf_space.yml` - GitHub Actions workflow to auto-sync changes with Hugging Face Space repo.
- `app.py` - Streamlit app source code for frontend.
- `Dockerfile` - Docker image build instructions for the Space.
- `my_model` - Local copy of the MLflow-registered XGBoost model.
- `mlruns` - MLflow experiment and model registry artifacts.
- Other scripts for model registration and verification.

## Auto-syncing with Hugging Face Space

This GitHub repo is **automatically synchronized** with the Hugging Face Space repository on every push to the `main` branch using a GitHub Actions workflow. This ensures the Hugging Face app is always updated with the latest code and model changes from this repo.

## Getting Started

To run this app locally:

1. Clone this repo:

```bash
git clone https://github.com/dglassbrenner1/hf_fraud_detection_space.git
```

2. Install dependencies (make sure Python 3.9+ is installed):

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Use the web interface to input transaction details and get fraud predictions.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
