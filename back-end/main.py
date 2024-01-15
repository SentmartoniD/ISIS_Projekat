from Controllers.data_controller import app
from Database import database
from Services import training_service, preprocessing_service, predict_service
from DatabaseFunctions import database_read_functions

def initialize_database_and_tables():
    database.create_database()
    database.create_us_holidays_table()
    database.create_load_data_table()
    database.create_weather_data_table()
    database.create_predicted_load_data_table()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_database_and_tables()
    app.run(debug=True)
    #training_service.train_model('2020-01-11', '2021-01-11')
    #rez = database_read_functions.read_from_weatherdata_table_by_date_and_days('2021-01-11', 2)
    #predict_service.predict('2020-01-11', 5)
    #training_service.train_model_and_predict()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
