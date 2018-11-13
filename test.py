import requests
from bs4 import BeautifulSoup, Comment

res = requests.get("https://www.basketball-reference.com/teams/TOR/2019.html",headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
data = []
data = []
table = soup.find('table', attrs={'id':'team_and_opponent'})
if table != None:
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele])
print(data)