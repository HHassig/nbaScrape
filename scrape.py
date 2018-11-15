import requests
from bs4 import BeautifulSoup, Comment
from prettytable import PrettyTable


# HTML Remover
def stripHTML(aTag):
	return aTag.get_text()
# Pre Work
numberOfPlayers = -1
teams = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
teamID = 13
url = "https://www.basketball-reference.com/teams/" + teams[teamID] + "/2019.html"
print(teams[teamID])

# Visit page and scrape
res = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(res.text, 'lxml')
for comment in soup.find_all(string=lambda text:isinstance(text,Comment)):
	data = BeautifulSoup(comment,"lxml")
	# Get team stats
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
	# Get player stats
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

# Finalize and clean data
teamHeader.pop(0)
for i in range(0, 8):
	teamHeader.pop()
team = PrettyTable()
team.field_names = teamHeader
team.add_row(allTeamStats[1])
team.add_row(allTeamStats[5])
print(team)

allPlayerStats.pop(0)
playerHeader.pop(0)
playerHeader.pop(0)
for i in range(0, numberOfPlayers):
	playerHeader.pop()
playerHeader.insert(0, "Name")
# Clean HTML from players
for i in range(len(allPlayerStats)):
	allPlayerStats[i][0] = stripHTML(allPlayerStats[i][0])
	allPlayerStats[i][2] = stripHTML(allPlayerStats[i][2])

player = PrettyTable()
player.field_names = playerHeader
for i in range(len(allPlayerStats)):
	player.add_row(allPlayerStats[i])
print(player)

