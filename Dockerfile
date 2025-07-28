# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files into container
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variable to production mode
ENV FLASK_ENV=production

# Run the app
CMD ["sh", "-c", "python addtodb.py && python app.py"]

