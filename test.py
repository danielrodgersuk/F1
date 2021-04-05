import requests
from bs4 import BeautifulSoup

Season_1950_HTML = requests.get("https://en.wikipedia.org/wiki/1950_Formula_One_season")

Season_1950_Soup = BeautifulSoup(Season_1950_HTML.text, 'html.parser')

Season_1950_Calendar_Soup_Header = Season_1950_Soup.find('table',{'class':'wikitable'}).findAll('th')
Season_1950_Calendar_Soup_Text = Season_1950_Soup.find('table',{'class':'wikitable'}).findAll('a')

for header in Season_1950_Calendar_Soup_Header:
	print(header)

for race in Season_1950_Calendar_Soup_Text:
	print(race.get("title"))