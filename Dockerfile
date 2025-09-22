# Use official Python 3.9 base image
FROM python:3.9

# Add non-root user for permissions compliance in HF Spaces
RUN useradd -m -u 1000 user

# Set working directory
WORKDIR /app

# Copy requirements.txt separately for Docker cache efficiency
COPY --chown=user ./requirements.txt requirements.txt

# Install dependencies including streamlit and mlflow (add to your requirements.txt if missing)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all app code
COPY --chown=user . /app

# Fix permissions
RUN mkdir -p /app/mlruns && chown -R user:user /app/mlruns

# Use non-root user
USER user

# Set environment variables for user path and app caches
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    STREAMLIT_HOME=/tmp/.streamlit \
    HF_HOME=/tmp/huggingface \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose Streamlit default port
EXPOSE 7860

# Run Streamlit app, binding to all interfaces and port 7860 (HF Spaces uses this port)
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
