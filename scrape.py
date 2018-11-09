import requests
from bs4 import BeautifulSoup, Comment

res = requests.get("https://www.basketball-reference.com/teams/TOR/2019.html",headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
    data = BeautifulSoup(comment,"lxml")
    for items in data.select("table tr"):
        tds = [item.get_text(strip=True) for item in items.select("th,td")]
        if tds[0] == "Team" or tds[0] == "Opponent":
        	print(tds)
