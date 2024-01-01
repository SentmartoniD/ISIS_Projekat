from flask import Flask, request, jsonify
from flask_cors import CORS
from Services import database_service
import pandas

app = Flask("Electric consumption forecast app")
CORS(app)


@app.route('/api/LoadData', methods=['POST'])
def load_data():
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        LOAD_DATA_FILES = request.files
        '''
        for key, file in LOAD_DATA_FILES.items():
            df = pandas.read_csv(file)
            row = df.iloc[3]
            print(row.index[0])
            print(row[row.index[0]])
            print(type(row[row.index[0]]))
            print(row.index[1])
            print(row[row.index[1]])
            print(type(row[row.index[1]]))
            print(row.index[2])
            print(row[row.index[2]])
            print(type(row[row.index[2]]))
            print(row.index[3])
            print(row[row.index[3]])
            print(type(row[row.index[3]]))
            print(row.index[4])
            print(row[row.index[4]])
            print(type(row[row.index[4]]))'''
        rez = database_service.fill_loaddata_table(LOAD_DATA_FILES)
        print(rez)
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/WeatherData', methods=['POST'])
def weather_data():
    if 'file1' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        WEATHER_DATA_FILES = request.files
        #rez = database_service.fill_weatherdata_table(WEATHER_DATA_FILES)
        #print(rez)
        return jsonify({'message': 'Files uploaded successfully'}), 200


@app.route('/api/USHolidaysData', methods=['POST'])
def us_holidays_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    else:
        US_HOLIDAYS_DATA_FILE = request.files['file']
        #rez = database_service.fill_usholidays_table(US_HOLIDAYS_DATA_FILE)
        #print(rez)
        return jsonify({'message': 'File uploaded successfully'}), 200


@app.route('/api/TrainModel', methods=['GET'])
def train_model():
    return True


@app.route('/api/BeginForecast', methods=['GET'])
def begin_forecast():
    return True
