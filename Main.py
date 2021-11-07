import requests


def GetImportantStats(data):

    """
    Parses a list of data of a single player. Pulls important data and stores it in
    dictionary

    :param data: List of data about a single player
    :return: dict
    """

    dataDictionary = {}

    FG3M = data[14]
    FGA = data[12]
    FGM = data[11]
    FTM = data[17]
    FTA = data[18]
    REB = data[22]
    AST = data[23]
    STL = data[25]
    BLK = data[26]
    TOV = data[24]


    dataDictionary["num_3points"] = FG3M
    dataDictionary["num_2points"] = FGM - FG3M
    dataDictionary["num_field_goals"] = FGA
    dataDictionary["num_free_throws_made"] = FTM
    dataDictionary["num_free_throws"] = FTA

    dataDictionary["rebounds"] = REB
    dataDictionary["assists"] = AST
    dataDictionary["steal"] = STL
    dataDictionary["blocks"] = BLK
    dataDictionary["turnovers"] = TOV

    return dataDictionary




def CalculateScore(dataDictionary):

    """
    Takes in dataDictionary --> Dictionary of data about a single player and calculates
    score.

    :param dataDictionary: dictionary
    :return: int
    """

    score = 0

    score += dataDictionary["num_3points"] * 6
    score += dataDictionary["num_2points"] * 4
    score += dataDictionary["num_free_throws_made"] * 2

    score += dataDictionary["rebounds"]
    score += dataDictionary["assists"] * 2
    score += dataDictionary["steal"] * 4
    score += dataDictionary["blocks"] * 4

    score -= dataDictionary["turnovers"] * 2

    score -= dataDictionary["num_field_goals"]
    score -= dataDictionary["num_free_throws"]

    return score


"""
The season id is hard coded.

Three url's for the the three positions.
Call each one of the url's seperately and parse each of the data sets.
"""

season_id = "2020-21"

center_url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=C&PlusMinus=N&Rank=N&Season=" + season_id +  "&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
forward_url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=F&PlusMinus=N&Rank=N&Season=" + season_id +  "&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
guard_url = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=G&PlusMinus=N&Rank=N&Season=" + season_id +  "&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="


headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


centerResponse = requests.get(url=center_url, headers=headers).json()
forwardResponse = requests.get(url=forward_url, headers=headers).json()
guardResponse = requests.get(url=guard_url, headers=headers).json()

#All data entries have the same format --> 2d list. Each sublists holds data about individual player such as id, name, fieldGoals, etc.

centerDataEntries = centerResponse["resultSets"][0]["rowSet"]
forwardDataEntries = forwardResponse["resultSets"][0]["rowSet"]
guardDataEntries = guardResponse["resultSets"][0]["rowSet"]




greatestPlayers = {"C": [0,""], "F": [(0, ""), (0, "")], "G": [(0, ""), (0, "")]}


"""
Calculating scores players whose position is center
"""

for data in centerDataEntries:

    dataDictionary = GetImportantStats(data)

    score = CalculateScore(dataDictionary)


    if score > greatestPlayers["C"][0]:

        greatestPlayers["C"] = [score, data[1].strip()]


"""
Calculating scores for players whose positions are forward
"""

for data in forwardDataEntries:

    dataDictionary = GetImportantStats(data)

    score = CalculateScore(dataDictionary)

    if score > greatestPlayers["F"][0][0]:

        greatestPlayers["F"][0] = (score, data[1])
        greatestPlayers["F"].sort()




for data in guardDataEntries:

    dataDictionary = GetImportantStats((data))

    score = CalculateScore(dataDictionary)

    if score > greatestPlayers["G"][0][0]:

        greatestPlayers["G"][0] = (score, data[1])
        greatestPlayers["G"].sort()


print(greatestPlayers)

