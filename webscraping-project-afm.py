import requests
from bs4 import BeautifulSoup
import re

# Creating different versions of the url with regex
# url = f'https://www.afm.nl/nl-nl/sector/registers/vergunningenregisters/financiele-dienstverleners/details?id={i}'
# i = re.findall("\w*-\w*-\w*-\w*-\w*", content)
# UNDER CONSTRUCTION

# Create dictionary with user-agent = Firefox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}

# Retrieve content from webpage
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content, 'html.parser')


# Scrape and find content based on class
list_results = soup.find_all('div', class_='cc-em--detail-list__items')

# Create empty list to store scraped content
results_list = []

# Loop over list, save content from every column, and add it to the final list
for result in list_results:
    for span in result.find_all('span', class_='cc-em--detail-list__value'):
        results_list.append(span.text.strip())


# Scrape and find content based on class
table_results = soup.find_all('table', class_='cc-table-wrap-text')

# Create empty list to store scraped content
results_table = []

# Loop over table, get the text content following the span element within the table data, and add it to the final list
for result in table_results:
    for span in result.find_all('span', class_='cc-mobile-title'):
        text_content = span.next_sibling
        results_table.append(text_content)


''' TO DO:
*Combine data in 1 list instead of 2
*Test regex
*Save as csv?
'''
