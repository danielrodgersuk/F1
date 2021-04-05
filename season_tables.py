import requests
from bs4 import BeautifulSoup
import pandas as pd

def Tables(year):

	Season_HTML = requests.get(f"https://en.wikipedia.org/wiki/{year}_Formula_One_season")

	Season_Soup = BeautifulSoup(Season_HTML.text, 'html.parser')

	Season_Tables_Soup = Season_Soup.findAll('table',{'class':'wikitable'})
	
	for table in Season_Tables_Soup:
		Season_Table_Soup = table.findAll('tr')
		
		Season_Table_Lists = []
		for row in Season_Table_Soup:
			Season_Table_Lists.append(row.text.strip().split('\n\n'))
			
		print(pd.DataFrame(Season_Table_Lists))

print(Tables(1950))