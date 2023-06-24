import os
import json
from utils import check_if_all_html, load_config_by_section
from bs4 import BeautifulSoup






class Scraper:
    def __init__(self,temp_path:str):
        if not temp_path:
            temp = load_config_by_section('paths')['temp_path']
        else:
            self.temp_path = temp_path
        
        if not os.path.exists(self.temp_path):
            raise ValueError(f'Temp Path does not exist. I was given {self.temp_path}')
        if not check_if_all_html(self.temp_path):
            raise ValueError ('Folder contains other files than html')
        
        
    def _load_config_params(self,name_params = 'css_selectors'):
        return load_config_by_section(name_params)

    def _load_soup_data(self,):
        soup_page:list[BeautifulSoup] = [] 
        for i in os.listdir(self.temp_path):
            full_path = os.path.join(f'../{self.temp_path}',i)
            print(i)
            with open(full_path,'r') as file:
                content = file.read()
            soup_page.append(BeautifulSoup(content))
        return soup_page

    
    def _convert_to_dataframe(self):
        res = []
        soup_page = self._load_soup_data()
        css_selectors = self._load_config_params()
        for page in self.soup_page:
            all_ads = page.select(css_selectors['ad'])
            print(len(all_ads))
            for car in all_ads:
                car_data = {}
                car_data['link'] = car.get('href')
                for name,selector in css_selectors.items():
                    if name == 'ad':
                        continue
                    else:
                        try:
                            car_data[name] = car.select_one(selector).text
                        except:
                            car_data[name] = 'N/A'
                res.append(car_data)

    def run  
        
        
        
    
    