from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = [] 

url = 'https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

html = requests.get(url, headers=headers).text


soup = BeautifulSoup(html, "lxml")

table = soup.find_all('table', class_= 'stats_table')[0]; 

links = table.find_all('a')
links = [l.get('href') for l in links]
links = [l for l in links if '/squads' in l]

team_urls = [f"https://fbref.com{l}" for l in links]

print(team_urls)