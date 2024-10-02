from flask import Flask, render_template, request, jsonify
import mysql.connector  
import pickle
import numpy as np

app = Flask(__name__)

# MySQL connection setup
connection = mysql.connector.connect(
    host='database-1.cf82qqe4y049.eu-north-1.rds.amazonaws.com',
    user='admin',
    password='R14TCkick',
    database='exldemo'
)


model = pickle.load(open('model/regmodel.pkl', 'rb'))
scaler = pickle.load(open('model/scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data-analysis')
def data_analysis():
    return render_template('analysis.html')

@app.route('/model-prediction')
def model_prediction():
    return render_template('predict.html')

# Route for prediction using form input (for model prediction page)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        scaled_data = scaler.transform(np.array(data).reshape(1, -1))  
        output = model.predict(scaled_data)[0]  
        
        if output < 4:
            comment = "Comment: Healthy"
        elif 4 <= output < 8:
            comment = "Comment: Moderately Polluted"
        else:
            comment = "Comment: Severely Polluted"
        return render_template('predict.html', prediction_text=f'The health risk score prediction is {output} || {comment}')
    except Exception as e:
        return render_template('predict.html', prediction_text=f"Error: {str(e)}")


@app.route('/max-temperature', methods=['GET'])
def max_temperature():
    try:
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT City, MAX(tempmax) AS max_temperature FROM urban_air_quality_data GROUP BY City ORDER BY max_temperature DESC LIMIT 10;")
        results = cursor.fetchall()
        cursor.close()

        
        if not results:
            return jsonify({"error": "No data found"}), 404

        return jsonify(results) 
    except Exception as e:
        
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Query 1: Min Temperature Cities
@app.route('/min-temperature', methods=['GET'])
def min_temperature():
    query = """
    SELECT City, MIN(tempmin) AS min_temperature
    FROM urban_air_quality_data
    GROUP BY City
    ORDER BY min_temperature ASC
    LIMIT 10;
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# Query 2: Average Humidity by City
@app.route('/avg-humidity', methods=['GET'])
def avg_humidity():
    query = """
    SELECT City, AVG(humidity) AS avg_humidity
    FROM urban_air_quality_data
    GROUP BY City
    ORDER BY avg_humidity DESC
    LIMIT 10;
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# Query 3: Top 5 Cities with Highest Health Risk Score
@app.route('/highest-health-risk', methods=['GET'])
def highest_health_risk():
    query = """
    SELECT City, MAX(Health_Risk_Score) AS highest_health_risk
    FROM urban_air_quality_data
    GROUP BY City
    ORDER BY highest_health_risk DESC
    LIMIT 5;
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# Query 4: Max Wind Speed by City
@app.route('/max-wind-speed', methods=['GET'])
def max_wind_speed():
    query = """
    SELECT City, MAX(windspeed) AS max_wind_speed
    FROM urban_air_quality_data
    GROUP BY City
    ORDER BY max_wind_speed DESC
    LIMIT 10;
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# Query 5: Days with Precipitation in a Given City
@app.route('/days-with-precipitation/<city>', methods=['GET'])
def days_with_precipitation(city):
    query = """
    SELECT COUNT(*) AS days_with_precipitation
    FROM urban_air_quality_data
    WHERE City = %s AND precip > 0;
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

