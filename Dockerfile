FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your bot files into the container
COPY . .

# Expose the server port (8080)
EXPOSE 8080

# Start both the bot and the aiohttp server
CMD ["python", "autoaccpt.py"]
