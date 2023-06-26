from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

stars = requests.get(START_URL)
ball  = BeautifulSoup(stars.text,'html.parser')

list = []
start_table = ball.find_all('table',{'class','wikitable sortable jquery-tablesorter'})
total_table = len(start_table)
table_rows = start_table[1].find_all('tr')
for i in table_rows:
    td = i.find_all('td')
    messeage  = [x.text.rstrip() for x in td]
    list.append(messeage)
star_names = []
mass = []
radius = []
distance = []
for i in range(1,len(list)):
    star_names.append(list[i][0])
    mass.append(list[i][7])
    radius.append(list[i][8])
    distance.append(list[1][5])
headers = ['star_names','distance','mass','radius']
data = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['star_names','distance','mass','radius'])
data.to_csv('project.csv',index=True,index_label='id')
                                                                    