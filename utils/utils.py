from configparser import ConfigParser

SECTIONS = ['css_selectors','options']


def load_config_params() -> dict:
    '''
    Function to load configurations
    '''
    params:dict = {}
    config = ConfigParser()
    config.read('scraper/gebrauctwagen/gebrauchtWagen_config.ini')
    sections = config.sections()
    for section in SECTIONS:
        if section not in sections:
            raise ValueError(f'Missing sections: {section}')
    params['css_selectors'] = dict(config['css_selectors'])
    params['options'] = dict(config['options'])
    return params


def get_connection_string():
    config = ConfigParser()
    config.read('config_app.ini')
    return config['database_info']['connection_string']


if __name__ == '__main__':
    load_config_params()
    get_connection_string()