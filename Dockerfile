# Use an official Python runtime as the base image
FROM python:3.13.2

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN apt-get update && apt-get install -y fonts-freefont-ttf

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run Streamlit on container start
CMD ["streamlit", "run", "master_chef.py"]
