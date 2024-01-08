import requests
from bs4 import BeautifulSoup
import re
import csv
import os.path

# Creating different versions of the url with regex
# url = f'https://www.afm.nl/nl-nl/sector/registers/vergunningenregisters/financiele-dienstverleners/details?id={i}'
# i = re.findall("\w*-\w*-\w*-\w*-\w*", content)
# UNDER CONSTRUCTION

url = 'https://www.afm.nl/nl-nl/sector/registers/vergunningenregisters/financiele-dienstverleners/details?id=C18B1D63-774C-E811-80D9-005056BB0C82'

# Create dictionary with user-agent = Firefox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}

# Retrieve content from webpage
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content, 'html.parser')


# Scrape and find content based on class
list_results = soup.find_all('div', class_='cc-em--detail-list__items')

# Create empty list to store scraped content with company info
register = []

# Loop over list, save content from every column, and add it to the final list
for result in list_results:
    for span in result.find_all('span', class_='cc-em--detail-list__value'):
        register.append(span.text.strip())


# Scrape and find table content
table_results = soup.find_all('tbody')

# Loop over table, get the text content following the span element within the table data, and add it to the final list
for tr in table_results:
    data = []
    for td in tr.find_all('td'):
        for span in td.find_all('span', class_='cc-mobile-title'):
            # Extract the text content after the span element within the td
            text_content = span.next_sibling
            data.append(text_content)

    register.append(data)


# TO DO:
# Get each tr on new row
# Save to csv
# Make regex work
