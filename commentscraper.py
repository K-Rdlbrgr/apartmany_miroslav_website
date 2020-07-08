import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as pdr
import pickle
import requests
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import csv
import random

# Create empty dics for final data collection
data = {}
f_data = {}

# Web Scraping the tickers from Wikipedia
def save_comments():
    
    driver = webdriver.Chrome(executable_path='/Users/kevin/Desktop/Python/Projects/DAX Performance/chromedriver')
    
    # Set URL to the iFrame source
    my_url = 'https://liptov.sk/rez/guestbook.php?input_hotel_id=253&lo=uk'
    print(my_url)
    
    # create a new Chrome session
    # driver = webdriver.Chrome(executable_path='/Users/kevin/Desktop/Python/Projects/DAX Performance/chromedriver')
    driver.implicitly_wait(10)
    driver.get(my_url)
    
    # Creating the soup object based on the text of the source code
    # Selenium hands the page source to Beautiful Soup
    soup = bs.BeautifulSoup(driver.page_source, 'lxml')
    
    # Using soup to find the particular bg tag with all relevant tables
    tables = soup.find('bg')
    
    names = []
    dates = []
    titles = []
    messages = []
    ratings = []
    pictures = []
    
    # Loop through all tables
    for table in tables.findAll('table')[1:-1]:
        name_date = table.findAll('tr')[0]
        name = name_date.find('a').string
        date = name_date.findAll('th')[1].string
        names.append(name)
        dates.append(date)
        
        message = table.findAll('tr')[1]
        message = message.find('td').text.strip()
        messages.append(message)
        
        rating = table.findAll('tr')[2]
        rating = rating.find('td')
        rating = round((len(rating.findAll('img'))+0.1)/2)
        ratings.append(rating)        

    
    temp_dates=[]
    for date in dates:
        hour = random.randint(10,23)
        minute = random.randint(10,59)
        second = random.randint(10,59)
        temp_dates.append(f'{date} {hour}:{minute}:{second}+00:00')
    dates = temp_dates
    
    for m in messages:
        titles.append(re.split('[.!]',m)[0])
        picture_rand = random.randint(1,50)
        pictures.append(f'apartmany/img/1 de 3 Avatars FLAT/Avatars Set Flat Style-{picture_rand}.png')
        
    data['names'] = names
    data['dates'] = dates
    data['titles'] = titles
    data['messages'] = messages
    data['ratings'] = ratings
    data['pictures'] = pictures
    
    # with open('comments.csv') as csvfile:
    #     reader = csv.DictReader(csvfile, delimiter='|')
    #     for row in reader:
    #         p = Comment(name=row['names'], title=row['titles'], rating=row['ratings'], content=row['messages'], date_posted=row['dates'], picture=row['pictures']) 
    #         p.save() 
    
    keys = sorted(data.keys())
    with open('comments.csv', 'w') as outfile:
        writer = csv.writer(outfile, delimiter = '|')
        writer.writerow(keys)
        writer.writerows(zip(*[data[key] for key in keys]))
    
    return data
    
save_comments()
        

            
    
    