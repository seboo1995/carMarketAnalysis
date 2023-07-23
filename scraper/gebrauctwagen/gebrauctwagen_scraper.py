import requests
import time
import pandas as pd
import os
from datetime import datetime
from bs4 import BeautifulSoup
from utils.utils import load_config_params


class GebrauchtWagenScraper:
    def __init__(self):
        self.params = load_config_params()
        self.res_list = []
    
    
    def _create_requests(self):
        '''
        This function will produce the responses
        '''
        max_pages = int(self.params['options']['max_pages'])
        timeout = int(self.params['options']['timeout_in_seconds'])
        base_url = self.params['options']['base_url']
        responses_list = []
        for i in range(1,max_pages):
            url = base_url+str(i)
            response = requests.get(url)
            if response.status_code != 200:
                raise ValueError(f'Status code for page{str(i)} was {response.status_code}')
                continue
            soup = BeautifulSoup(response.text,features='html')
            responses_list.append(soup)
            time.sleep(timeout)
        return responses_list
    
    
    def get_data_from_responeses(self):
        '''
        Converts the soups to 
        
        '''
        responses_soups = self._create_requests()
        css_selectors = self.params['css_selectors']
        temp_path = self.params['options']['temp_path']
        # first get indiividual ads
        for page in responses_soups:
            print('Page: '+ str(responses_soups.index(page)))
            all_ads_in_page = page.select(css_selectors['ad_selector'])
            for individual_ad in all_ads_in_page:
                temp_dict = {}
                for col_name,css_selector in css_selectors.items():
                    if col_name == 'ad_selector':
                        continue
                    temp_dict[col_name] = individual_ad.select(css_selector)[0].text
                self.res_list.append(temp_dict)
        df = pd.DataFrame(self.res_list)
        if  not os.path.exists(temp_path):
            os.mkdir(temp_path)

        df.to_csv(f'{os.path.join(temp_path,self.make_fileName())}',index=False)
        return f'{os.path.join(temp_path,self.make_fileName())}'
    
    
    def make_fileName(self):
        return datetime.now().strftime('%d-%b-%y') +'.csv'