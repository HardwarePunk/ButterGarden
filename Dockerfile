# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create volume for persistent database storage
VOLUME ["/app/instance"]

# Run as non-root user
RUN useradd -m myuser
RUN chown -R myuser:myuser /app
USER myuser

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
