import requests
from bs4 import BeautifulSoup, Comment
from prettytable import PrettyTable

numberOfPlayers = -1
teams = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
url = "https://www.basketball-reference.com/teams/" + teams[3] + "/2019.html"
res = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
	data = BeautifulSoup(comment,"lxml")
	x = data.find("table", id="team_and_opponent")
	if x != None:
		allTeamStats = []
		teamHeader = []
		for tag1 in x.find_all("th"):
			teamHeader += tag1.contents
		for tag in x.find_all("tr"):
			rows = []
			for tag2 in tag.find_all("td"):
				rows += tag2.contents
			allTeamStats += [rows]
	y = data.find("table", id="per_game")
	if y != None:
		allPlayerStats = []
		playerHeader = []
		for tag1 in y.find_all("th"):
			playerHeader += tag1.contents
		for tag in y.find_all("tr"):
			numberOfPlayers += 1
			rows = []
			for tag2 in tag.find_all("td"):
				if not tag2.contents:
					tag2.contents = ["0.0"]
				rows += tag2.contents
			allPlayerStats += [rows]
allPlayerStats.pop(0)
playerHeader.pop(0)
playerHeader.pop(0)
for i in range(0, numberOfPlayers):
	playerHeader.pop()
playerHeader.insert(0, "Name")
player = PrettyTable()
player.field_names = playerHeader
for i in range(len(allPlayerStats)):
	player.add_row(allPlayerStats[i])
print(player)


teamHeader.pop(0)
for i in range(0, 8):
	teamHeader.pop()
team = PrettyTable()
team.field_names = teamHeader
team.add_row(allTeamStats[1])
team.add_row(allTeamStats[5])
print(team)