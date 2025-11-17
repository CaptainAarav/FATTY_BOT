FROM python:3.13-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything into the container
COPY . .

# Ensures logs show up instantly
ENV PYTHONUNBUFFERED=1

# Run your bot
CMD ["python3", "bot.py"]