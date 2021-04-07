import requests
from bs4 import BeautifulSoup
import pandas as pd

def Calendar(year):

	Season_HTML = requests.get(f"https://www.formula1.com/en/results.html/{year}/races.html")

	Season_Soup = BeautifulSoup(Season_HTML.text, "html.parser")

	Season_Calendar_Soup = Season_Soup.find("table",{"class":"resultsarchive-table"}).findAll("tr")

	Season_Calendar_Header = []
	Season_Calendar_Races = []
	
	for race in Season_Calendar_Soup:
		Season_Calendar_Fields = race.findAll("th")
		for field in Season_Calendar_Fields:
			Season_Calendar_Header.append(field.text.strip())

		Season_Calendar_Lists = race.findAll("td")
		Season_Calendar_Race = []
		for field in Season_Calendar_Lists:
			Season_Calendar_Race.append(field.text.strip().replace("\n", " "))
		Season_Calendar_Races.append(Season_Calendar_Race)
	
	Calendar = pd.DataFrame(Season_Calendar_Races, columns=Season_Calendar_Header)

	return Calendar
    
def Calendars(year1, year2):
	calendars = pd.DataFrame()
	for year in range(1+year2-year1):
		calendars = calendars.append(Calendar(year+year1),ignore_index=True)
	return calendars

print(Calendars(1950,2021))
# Next step: deal with none