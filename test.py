import requests
from bs4 import BeautifulSoup

Season_1950_HTML = requests.get("https://en.wikipedia.org/wiki/1950_Formula_One_season")

Season_1950_Soup = BeautifulSoup(Season_1950_HTML.text, 'html.parser')

Season_1950_Calendar_Soup = Season_1950_Soup.find('table',{'class':'wikitable'}).findAll('a')

for race in Season_1950_Calendar_Soup:
	print(race.get("title"))