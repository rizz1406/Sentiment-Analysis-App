# model/Dockerfile
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the model code to the container
COPY . .

# Install dependencies
RUN pip install flask textblob

# Expose the port for the Flask app
EXPOSE 5001

# Run the model server
CMD ["python", "sentiment_model.py"]
