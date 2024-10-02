# Urban Air Quality Risk Prediction App

This project is a web-based application for predicting urban air quality and health risks based on various environmental factors such as temperature, humidity, wind speed, etc. The app utilizes machine learning models to provide risk predictions and insights.

## Folder Structure

- **app.py**: The main backend file that runs the Flask server.
- **templates/**: This folder contains the HTML files for the app:
  - `home.html`: The homepage with navigation options.
  - `analysis.html`: Displays data analysis results.
  - `predict.html`: The form for inputting environmental data and displaying predictions.

## Setup Instructions

### Prerequisites
- Ensure you have access to your AWS EC2 instance with the necessary permissions.

### Steps to Run

1. **SSH into your EC2 Instance**  
   Open your terminal or command prompt and run the following command to SSH into your EC2 instance:
   
   ```bash
   ssh -i "C:\Users\Dell\Downloads\hrituraj-team4.pem" ubuntu@13.51.37.85

2. **Activate the Python Virtual Environment**
Once inside the EC2 instance, navigate to the project folder (if not already there) and activate the Python virtual environment:
   cd /home/ubuntu/Team_4_Project
   source myenv/bin/activate

3. **Install Required Dependencies**
If it’s the first time running the project or the dependencies are not installed, install the necessary Python libraries. You can do this using pip with the requirements.txt file (if available):
   pip install -r requirements.txt

4. **Run the Application**
After activating the environment and installing the dependencies, run the Flask app:
   python3 app.py

5. **Access the Application**
Once the app is running, you can access it by entering the following in your browser:
   http://13.51.37.85:5000
   


