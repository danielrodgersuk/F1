import requests
from bs4 import BeautifulSoup
import pandas as pd

def Calendar(year):

	Season_HTML = requests.get(f"https://en.wikipedia.org/wiki/{year}_Formula_One_season")

	Season_Soup = BeautifulSoup(Season_HTML.text, 'html.parser')

	Season_Calendar_Soup = Season_Soup.find('table',{'class':'wikitable'}).findAll('tr')

	Season_Calendar_Lists = [] 
	for race in Season_Calendar_Soup:
		Season_Calendar_Lists.append(race.text.strip().split('\n\n'))

	Season_Calendar_Header = Season_Calendar_Lists[0]
	Season_Calendar_Lists = Season_Calendar_Lists[1:]

	Calendar = pd.DataFrame(Season_Calendar_Lists, columns=Season_Calendar_Header)
	Calendar['Date'] = pd.to_datetime(Calendar['Date'] + ' ' + f'{year}')
	return Calendar[['Rnd','Date','Race','Circuit']]

def Calendars(year1, year2):
	calendars = pd.DataFrame(columns=['Rnd','Date','Race','Circuit'])
	for year in range(1+year2-year1):
		calendars = calendars.append(Calendar(year+year1),ignore_index=True)
	return calendars

print(Calendars(1950,1963))