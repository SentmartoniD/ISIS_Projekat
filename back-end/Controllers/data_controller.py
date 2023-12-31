from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas
from Services import database_service

app = Flask("Electric consumption forecast app")
CORS(app)


@app.route('/api/LoadData', methods=['POST'])
def load_data():
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        LOAD_DATA_FILES = request.files
        #database_service.fill_loaddata_table(LOAD_DATA_FILES)
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/WeatherData', methods=['POST'])
def weather_data():
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        WEATHER_DATA_FILES = request.files
        #database_service.fill_weatherdata_table(WEATHER_DATA_FILES)
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/USHolidaysData', methods=['POST'])
def us_holidays_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        US_HOLIDAYS_DATA_FILE = request.files['file']
        # database_service.fill_usholidays_table(US_HOLIDAYS_DATA_FILE)
        return jsonify({'message': 'File uploaded successfully'}), 200


@app.route('/api/TrainModel', methods=['GET'])
def train_model():
    return True


@app.route('/api/BeginForecast', methods=['GET'])
def begin_forecast():
    return True


"""
if __name__ == '__main__':
    app.run(debug=True)
"""