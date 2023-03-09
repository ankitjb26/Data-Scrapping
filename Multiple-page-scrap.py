#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[8]:


# Read the input file
df = pd.read_excel('Input.xlsx')

# Loop through each row in the input file
for index, row in df.iterrows():

    # Get the URL and URL_ID from the input file
    url = row['URL']
    url_id = row['URL_ID']

    # Make a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the article title
    
    for title in soup.find_all('title'):
        print(title.get_text())
        
     #Extract the article information
    
    for article in soup.find_all('div', class_='td-post-content'):
        print(article.get_text(strip=True, separator=' '))

    # Save the article text in a text file with URL_ID as its file name
    
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(f'{title}\n\n{article}')

    print(f'Successfully extracted and saved the article for {url_id}')


# In[ ]:




