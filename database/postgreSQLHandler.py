from utils.utils import get_connection_string
from sqlalchemy import create_engine
from configparser import ConfigParser
import pandas as pd


def create_postgre_engine():
    return create_engine(get_connection_string())



def save_csv_as_table(csv_file_path):
    engine = create_engine(get_connection_string())
    df = pd.read_csv(csv_file_path)
    df.to_sql('carTable',engine,if_exists='append')
