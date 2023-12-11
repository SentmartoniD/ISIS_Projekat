from flask import Flask
from flask_cors import CORS

app = Flask("Electric consumption forecast app")
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


@app.route('/api/LoadData', methods=['POST'])
def load_data():
    return "<p>Hi!</p>"


@app.route('/api/WeatherData', methods=['POST'])
def weather_data():
    return True


@app.route('/api/USHolidaysData', methods=['POST'])
def us_holidays_data():
    return True


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