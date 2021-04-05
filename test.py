import requests
from bs4 import BeautifulSoup
import pandas as pd

Season_1950_HTML = requests.get("https://en.wikipedia.org/wiki/1950_Formula_One_season")

Season_1950_Soup = BeautifulSoup(Season_1950_HTML.text, 'html.parser')

Season_1950_Calendar_Soup = Season_1950_Soup.find('table',{'class':'wikitable'}).findAll('tr')

Season_1950_Calendar_Lists = [] 
for race in Season_1950_Calendar_Soup:
	Season_1950_Calendar_Lists.append(race.text.strip().split('\n\n'))

Season_1950_Calendar = pd.DataFrame(Season_1950_Calendar_Lists)