# Use an official Python runtime as a parent image
# FROM python:3.9-slim


# ENV SUITECRM_DATABASE_PASSWORD=bitnami123

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container
# COPY ./fastapi_app /app 

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt & pip install --upgrade pip

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run app.py when the container launches
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.9

# Install dependencies
RUN pip install -r requirements.txt & pip install --upgrade pip 
RUN pip install uvicorn fastapi 
RUN pip install SQLAlchemy mysql-connector-python databases

# Copy the FastAPI app files
COPY . /app

WORKDIR /app

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

