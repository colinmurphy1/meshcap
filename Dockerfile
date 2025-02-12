# Use an official Python image as a base
FROM python:3.12-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV CHROMIUM_PATH=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromium-driver

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script into container
COPY screenshot.py .

# Command to run the script
CMD ["python", "screenshot.py"]
