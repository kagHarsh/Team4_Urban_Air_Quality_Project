# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Copy the PySpark script into the Docker container
COPY . /app

# Default command to run the PySpark job
CMD ["spark-submit", "main.py"]
