# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose a volume for storing downloaded files and SQLite database
VOLUME ["/app/data", "/app/db"]

# Run main.py when the container launches
# CMD ["python", "src/main.py"]
