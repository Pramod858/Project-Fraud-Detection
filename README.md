# Credit Card Fraud Detection Project

## For Dataset [Click here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Project needs `python > 3.9` version to run

![Screenshot 2023-11-16 183703](https://github.com/Pramod858/Project-Fraud-Detection/assets/80105491/becc17e9-60b1-4fb7-a905-278d50afef1a)

This project implements a Credit Card Fraud Detection system using machine learning. It includes a Flask web application with a Swagger API documentation, and the model is containerized using Docker for easy deployment.

## Overview

The goal of this project is to detect fraudulent credit card transactions through a machine learning model. The web application allows users to input transaction features, and the system predicts whether the transaction is fraudulent or not.

## Features

- Machine Learning Model: Trained model for predicting fraud based on transaction features.
- Flask Web Application: Provides a user-friendly interface for making predictions.
- Swagger API Documentation: Allows developers to understand and interact with the API endpoints.
- Docker Containerization: Simplifies deployment and ensures consistency across different environments.

## Usage

Follow these steps to build and run the project in a Docker container:

1. **Build Docker Image:**
    ```bash
    docker build -t <your_image_name> -f Dockerfile .
    ```

2. **Run Docker Container:**
    ```bash
    docker run -p 5000:5000 --name <your_container_name> <your_image_name>
    ```

3. **Access the Application:**
    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

4. **Stop the Container:**
    ```bash
    docker stop <your_container_name>
    ```

5. **Remove the Container:**
    ```bash
    docker rm <your_container_name>
    ```

6. **Remove the Image:**
    ```bash
    docker rmi <your_image_name>
    ```

7. **Clean Resources:**
    ```bash
    docker system prune
    ```

## Web Interface

The web interface provides input fields for transaction features (V1 to V28 and Amount). Enter the values and click the "Predict" button to see the prediction result.

## API Documentation

For detailed API documentation, visit [Swagger API Documentation](http://localhost:5000/apidocs).


