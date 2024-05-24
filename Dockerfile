# Use Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install requests

# Copy the Python script to fetch data
COPY fetch_huggingface_data.py /app

# Run the Python script when the container launches
CMD ["python", "fetch_huggingface_data.py"]

