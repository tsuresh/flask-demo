# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=starter.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["python", "starter.py"]
