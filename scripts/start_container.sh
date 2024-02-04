#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull pramod858/fraud-detection-app

# Run the Docker image as a container
docker run -d -p 5000:5000 pramod858/fraud-detection-app