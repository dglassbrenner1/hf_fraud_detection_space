# Use official Python 3.9 base image for better compatibility with HF Spaces
FROM python:3.9

# Add a non-root user to avoid permission issues in HF Spaces
RUN useradd -m -u 1000 user

# Set the working directory
WORKDIR /app

# Copy requirements.txt separately to leverage Docker cache
COPY --chown=user ./requirements.txt requirements.txt

# Install Python dependencies (you can pin versions in requirements.txt)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all app code
COPY --chown=user . /app

# Switch to user for safer execution
USER user

# Set environment variables for the user path
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Expose required port 7860 for Hugging Face Spaces
EXPOSE 7860

# Launch FastAPI app with uvicorn on port 7860 for HF Spaces
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
