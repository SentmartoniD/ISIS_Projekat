from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas

app = Flask("Electric consumption forecast app")
CORS(app)
# app.config['MAX_CONTENT_LENGTH'] = 7000 * 1024 * 1024

US_HOLIDAYS_DATA_FILE = 0
WEATHER_DATA_FILES = 0
LOAD_DATA_FILES = []


@app.route('/api/LoadData', methods=['POST'])
def load_data():
    # print('Request payload size:', request.content_length / (1024 * 1024), 'MB')
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        LOAD_DATA_FILES.append(request.files)
        print(LOAD_DATA_FILES.__len__())
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/WeatherData', methods=['POST'])
def weather_data():
    # print('Request payload size:', request.content_length / (1024 * 1024), 'MB')
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        WEATHER_DATA_FILES = request.files
        print(WEATHER_DATA_FILES)
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/USHolidaysData', methods=['POST'])
def us_holidays_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        US_HOLIDAYS_DATA_FILE = request.files['file']
        df = pandas.read_excel(US_HOLIDAYS_DATA_FILE)
        print(df)
        print(US_HOLIDAYS_DATA_FILE)
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