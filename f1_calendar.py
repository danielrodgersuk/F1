import requests
from bs4 import BeautifulSoup
import pandas as pd

def Calendar(year):

	SeasonHTML = requests.get(f"https://en.wikipedia.org/wiki/{year}_Formula_One_season")

	SeasonSoup = BeautifulSoup(SeasonHTML.text, 'html.parser')

	SeasonCalendar_Soup = SeasonSoup.find('table',{'class':'wikitable'}).findAll('tr')

	SeasonCalendar_Lists = [] 
	for race in SeasonCalendar_Soup:
		SeasonCalendar_Lists.append(race.text.strip().split('\n\n'))

	return pd.DataFrame(SeasonCalendar_Lists)

print(Calendar(1950))