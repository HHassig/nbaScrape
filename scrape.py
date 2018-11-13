import requests
from bs4 import BeautifulSoup, Comment

res = requests.get("https://www.basketball-reference.com/teams/TOR/2019.html",headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
    data = BeautifulSoup(comment,"lxml")
    x = data.find("table", id="team_and_opponent")
    if x != None:
    	total = []
    	header = []
    	for tag1 in x.find_all("th"):
    		header += [tag1.contents]
    	for tag in x.find_all("tr"):
    		rows = []
    		for tag2 in tag.find_all("td"):
    			rows += [tag2.contents]
    		total += [rows]
print(total)
print(header)