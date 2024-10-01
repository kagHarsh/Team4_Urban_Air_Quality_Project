# Team4_Urban_Air_Quality_Project

This project focuses on analyzing urban air quality, training machine learning models to predict health risk scores, and creating a web app for real-time predictions. The project also includes an automated pipeline using Jenkins and Docker, with deployment on AWS. Below are the details for all tasks of the project.

---

## Table of Contents
1. [Overview](#overview)
2. [Task 1: Data Cleaning, Visualization, and Model Training](#task-1-data-cleaning-visualization-and-model-training)
3. [Task 2: Web Application with Flask](#task-2-web-application-with-flask)
4. [Task 3: Jenkins Pipeline and AWS Deployment](#task-3-jenkins-pipeline-and-aws-deployment)
5. [Setup Instructions](#setup-instructions)
6. [Running the Application](#running-the-application)
7. [Future Work](#future-work)

---

## Overview

The goal of this project is to analyze urban air quality data, clean the data, visualize patterns, train machine learning models, and provide a web-based interface for users to input real-time air quality data and receive health risk predictions. In addition, a CI/CD pipeline is implemented using Jenkins and Docker, and the project is deployed on AWS for scalability.

### Project Parts:
1. **Data Cleaning, Visualization, and Model Training**: Cleaning the dataset, visualizing key patterns, and training machine learning models.
2. **Web Application (Flask)**: A simple web app where users can input data to predict health risk scores.
3. **Pipeline Automation and AWS Deployment**: Automating the deployment process using Jenkins and Docker, and deploying the project on AWS using EC2 and RDS.

---

## Task 1: Data Cleaning, Visualization, and Model Training

This task focuses on loading, cleaning, visualizing, and analyzing the urban air quality dataset. After processing, machine learning models are trained to predict health risk scores.

### Steps Involved:
1. **Data Cleaning**: 
   - Handle missing values.
   - Convert categorical values to numeric (via `StringIndexer`).
   - Remove duplicates and outliers.

2. **Visualization**:
   - Generate plots to visualize trends in temperature, humidity, pollution levels, etc.
   - Understand feature correlations using a heatmap.

3. **Model Training and Testing**:
   - Use machine learning algorithms such as Linear Regression, and, Decision Tree, Random Forest.
   - Evaluate models using metrics like Mean Squared Error (MSE) and R-squared.

#### Example Python File:
```bash
- main.py  # Script for data cleaning, visualization, and model training.
```

## Task 2: Web Application with Flask

In this task, we develop a web application using Flask to provide real-time health risk predictions based on user input. Users will be able to input air quality data via a web form, and the trained machine learning model will predict the health risk score, which will be displayed on the web page.

---

### Web Application Features:
- **User Input**: The web application accepts user inputs for air quality parameters.
- **Model Prediction**: Based on the input values, the model trained in Task 1 predicts the health risk score.
- **Web Form**: The frontend provides a simple form for users to input required parameters.
- **Flask Backend**: The Flask framework handles requests, invokes the machine learning model, and returns the prediction results to the user.

### Steps to Build the Web Application:

#### 1. Create the Flask Application (`app.py`):

- **Flask Framework**: We use Flask to set up the backend that will handle user requests and predict health risk scores using the trained machine learning model.
- **Load the Trained Model**: The trained model from Task 1 is loaded using `joblib` or `pickle` to make predictions based on user input.

#### Key Flask Routes:
