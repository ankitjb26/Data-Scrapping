
# first installed Beutifulsoup4 liabrary for web scrap
# 
# pip install requests - for making HTTP requests.
# 
# pip install lxml - To extract data from HTML text
# 
# pip install urllib3 - urllib is a package that allows you to access the webpage with the program.
# 
# 
## import necessary library
import requests
from bs4 import BeautifulSoup
import pandas as pd


# ## Define the URL of the article to scrape

url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes'
result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, 'lxml')
print("This is soup",soup.prettify())

# ## Scrape article in HTML parser
soup1 = BeautifulSoup(result.content, 'html.parser')
print("This is soup1")
print(soup1.prettify())

soup1.findAll(attrs = {'class': 'td-post-content'})


# ## Get the title of page
# ### displaying title

print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())


# ## Scrape the article information

transcript = soup1.find('div', class_='td-post-content')
transcript = transcript.get_text(strip=True, separator=' ')


# ## Displyaing Article information
print(transcript)


# # export data into .txt file
data = str([[title,transcript]]).replace('<title>',"") #TypeCasting List-->String
data=data.replace('</title>',"")
print(data)
type(data)
with open('37.txt', 'w') as file:
    file.write(data)
