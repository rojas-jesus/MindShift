FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create and switch to a non-root user
RUN adduser --disabled-password --gecos "" django-user

# Make entrypoint script executable and change ownership
RUN chmod +x entrypoint.sh && \
    chown django-user:django-user entrypoint.sh

USER django-user

# Port used by Django (Render.com will map this)
EXPOSE 8000

# Use entrypoint script for flexible port configuration
CMD ["./entrypoint.sh"]
