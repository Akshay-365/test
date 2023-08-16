# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the contents of the app directory to the container
COPY . /app

# Install required packages
RUN pip install Flask gradio

# Expose port 80 for the Flask app
EXPOSE 80

# Start the Flask app when the container runs
CMD ["python", "app.py"]
