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
    for td in tr.find_all('td'):
        for span in td.find_all('span', class_='cc-mobile-title'):
            # Extract the text content after the span element within the td
            text_content = span.next_sibling
            register.append(text_content)

#
# # Before saving the file, check if already exists
# file_exists = os.path.isfile("Register_AFM_Output.csv")
#
# # Create new csv file to add data to
# with open("Register_AFM_Output.csv", "a", newline='') as file:
#     headers = ["Statutaire_naam", "Handelsnaam", "Vergunningnummer", "Adres", "Land", "KvK", "Financiele_dienst", "Product", "Begindatum", "Einddatum"]
#
#     writer = csv.DictWriter(file, delimiter=',', fieldnames=headers, extrasaction='ignore', dialect='unix')
#
#     # Only add headers when the file is newly created
#     if not file_exists:
#         writer.writeheader()
#
#     # Loop over every result on business page
#     for item in company_info:
#         writer.writerow(item)
#
# print('Company information retrieved!')

# TO DO:
# Get each tr on new row
# Make csv save work
# Make regex work
