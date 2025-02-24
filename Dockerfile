# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update -y && apt-get install -y awscli
# Upgrade pip
RUN pip install --upgrade pip
# Install requirements
RUN pip install --no-cache-dir -r requirements.txt
# Install sqlite3
RUN apt-get install -y sqlite3 libsqlite3-dev

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
# app.py is the entrypoint of the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
