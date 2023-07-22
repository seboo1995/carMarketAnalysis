from gebrauctwagen.gebrauctwagen_scraper import GebrauchtWagenScraper
from sqliteHandler import save_csv_as_table


gebrauchtScraper = GebrauchtWagenScraper()
fileName = gebrauchtScraper.get_data_from_responeses()
save_csv_as_table(fileName)


