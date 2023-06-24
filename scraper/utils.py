import os
from configparser import ConfigParser

def check_if_all_html(path):
    if not os.path.exists(path):
        raise ValueError (f'{path} does not exist')
    for file in os.listdir(path):
        if '.html' not in file:
            raise ValueError(f'{file} is not an html file')
    return True


def load_config_file(config_file_path:str = 'scraper/config.cfg'):
    if not os.path.exists(config_file_path):
        print('Does Not Exists')
    config_parser = ConfigParser()
    config_parser.read(config_file_path)
    print(config_parser.sections())
    return config_parser

def load_config_by_section(name):
    config_parser = load_config_file()
    return dict(config_parser[name])

