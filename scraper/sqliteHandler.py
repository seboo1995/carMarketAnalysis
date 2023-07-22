from sqlalchemy import create_engine
import pandas as pd
from configparser import ConfigParser

def get_connection_string():
    config = ConfigParser()
    config.read('scraper/config_app.ini')
    return config['database_info']['connection_string']




def save_csv_as_table(csv_file_path):
    engine = create_engine(get_connection_string)
    df = pd.read_csv(csv_file_path)
    df.to_sql('carTable',engine)

