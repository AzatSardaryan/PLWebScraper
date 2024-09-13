from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = [] 

url = 'https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats'


html = requests.get(url).text


soup = BeautifulSoup(html, "lxml")

table = soup.find_all('table', class_= 'stats_table')[0]; 

links = table.find_all('a')
links = [l.get('href') for l in links]
links = [l for l in links if '/squads' in l]

team_urls = [f"https://fbref.com{l}" for l in links]

for team_url in team_urls:
    team_name = team_url.split("/")[-1].replace("-Stats", "")
    data = requests.get(team_url).text
    soup = BeautifulSoup(data, "lxml")
    stats = soup.find_all("table", class_ = "stats_table")[0]

    if stats and stats.columns: stats.columns = stats.columns.droplevel(0)
    team_data = pd.read_html(str(stats))[0]
    team_data["Team"] = team_name
    all_teams.append(team_data)
    time.sleep(10)

stat_df = pd.concat(all_teams)
stat_df.to_csv("stats.csv")