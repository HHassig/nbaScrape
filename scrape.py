import requests
from bs4 import BeautifulSoup, Comment

res = requests.get("https://www.basketball-reference.com/teams/TOR/2019.html",headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
    data = BeautifulSoup(comment,"lxml")
    x = data.find("table", id="team_and_opponent")
    if x != None:
    	for tag in x.find_all("td"):
    		print(tag.contents)