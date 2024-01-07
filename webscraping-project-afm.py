import requests
from bs4 import BeautifulSoup
import re

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
for tr in table_results:
    data = []
    for td in tr.find_all('td'):
        for span in td.find_all('span', class_='cc-mobile-title'):
            # Extract the text content after the span element within the td
            text_content = span.next_sibling
            data.append(text_content)
    results_table.append(data)

print(results_table)
#
# for row in results_table:
#     company_info = results_list + results_table
#
# print(company_info)

''' TO DO:
*Combine data in 1 list instead of 2
*Test regex
*Save as csv?
'''
