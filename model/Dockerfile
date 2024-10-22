# model/Dockerfile
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the model code to the container
COPY . .

# Expose the port for the Flask app
EXPOSE 5001

# Run the model server
CMD ["python", "sentiment_model.py"]
