# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files for the microservice
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port (e.g., 5000 for add, 5001 for subtract, etc.)
EXPOSE 5000

# Start the microservice
CMD ["python", "divide.py"]
