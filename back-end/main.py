from Controllers.data_controller import app
from Database import database
from Services import preprocessing_service

def initialize_database_and_tables():
    database.create_database()
    database.create_us_holidays_table()
    database.create_load_data_table()
    database.create_weather_data_table()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_database_and_tables()
    #app.run(debug=True)
    preprocessing_service.preprocess()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
