from Controllers.data_controller import app
from Database.database import create_database

# initialize_database_and_tables

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_database()
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
