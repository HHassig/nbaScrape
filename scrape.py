import requests
from bs4 import BeautifulSoup, Comment
from prettytable import PrettyTable
import time

# HTML Remover
def stripHTML(aTag):
	return aTag.get_text()

# Pre Work
teams = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
teams = ["LAL", "GSW"]
everyTeam = []
everyPlayer = []
for teamID in range(len(teams)):
	time.sleep(10)
	# Visit page and scrape
	print(teams[teamID])
	print(teamID)
	numberOfPlayers = -1
	url = "https://www.basketball-reference.com/teams/" + teams[teamID] + "/2019.html"
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
	print(len(teamHeader))
	print(len(allTeamStats[2]))
	for i in range(0, 8):
		teamHeader.pop()
	for i in range(0, 17):
		teamHeader.pop(0)
	for i in range(0, 15):
		allTeamStats[2].pop(0)
		allTeamStats[6].pop(0)
	teamHeader.pop(5)
	allTeamStats[2].pop(5)
	allTeamStats[6].pop(5)
	team = PrettyTable()
	team.field_names = teamHeader
	team.add_row(allTeamStats[2])
	team.add_row(allTeamStats[6])
	print(team)
	everyTeam += [allTeamStats[1], allTeamStats[5]]


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
		everyPlayer += [allPlayerStats[i]]
	# print(player)
print(everyTeam)
print(everyPlayer)