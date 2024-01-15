from flask import Flask, request, jsonify
from flask_cors import CORS
from Services import database_service, training_service, predict_service
import pandas

app = Flask("Electric consumption forecast app")
CORS(app)


@app.route('/api/LoadData', methods=['POST'])
def load_data():
    try:
        if 'file1' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        else:
            LOAD_DATA_FILES = request.files
            result = database_service.fill_loaddata_table(LOAD_DATA_FILES)
            print(result)
            return jsonify({'message': 'Files uploaded successfully'}), 200
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return jsonify({'message': error_message}), 500


@app.route('/api/WeatherData', methods=['POST'])
def weather_data():
    try:
        if 'file1' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        else:
            WEATHER_DATA_FILES = request.files
            result = database_service.fill_weatherdata_table(WEATHER_DATA_FILES)
            print(result)
            return jsonify({'message': 'Files uploaded successfully'}), 200
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return jsonify({'message': error_message}), 500


@app.route('/api/USHolidaysData', methods=['POST'])
def us_holidays_data():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        else:
            US_HOLIDAYS_DATA_FILE = request.files['file']
            result = database_service.fill_usholidays_table(US_HOLIDAYS_DATA_FILE)
            print(result)
            return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return jsonify({'message': error_message}), 500


@app.route('/api/TrainModel', methods=['POST'])
def train_model():
    try:
        data = request.json
        startDate = data.get('startDate')
        endDate = data.get('endDate')
        training_service.train_model(startDate, endDate)
        return jsonify({'message': "Trening uspiješno izvršen!"}), 200
    except Exception as e:
        return jsonify({'message': "Pogresni datumi izabrani, izaberite ponovo!"}), 500


@app.route('/api/BeginForecast', methods=['POST'])
def begin_forecast_action():
    try:
        data = request.json
        startDate = data.get('startDate')
        days = data.get('days')
        predict_service.predict(startDate, int(days))
        return jsonify({'message': 'Prognoza uspesna!'}), 200
    except Exception as e:
        return jsonify({'message': "Pogresan datum je izabran, izaberite ponovo!"}), 500


@app.route('/api/ShowData', methods=['POST'])
def begin_forecast():
    try:
        data = request.json
        startDate = data.get('startDate')
        endDate = data.get('endDate')
        data_list = database_service.get_from_predictedloaddata_table_by_dates(startDate, endDate)
        if data_list.__len__() == 0:
            return jsonify({'message': "Pogresni datumi izabrani, izaberite ponovo!"}), 500
        else:
            return jsonify({'data_list': data_list, 'message': 'Uspesno primljeni podaci'}), 200
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return jsonify({'message': error_message}), 500
