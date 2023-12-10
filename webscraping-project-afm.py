import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.afm.nl/nl-nl/sector/registers/vergunningenregisters/financiele-dienstverleners'

# Create dictionary with user-agent = Firefox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}

# Add user-agent Firefox to url
response = requests.get(url, headers=headers)
content = response.content

# Scrape and find content based on class
soup = BeautifulSoup(content, 'html.parser')
results = soup.find_all('tr', class_='jq_registers_register-paged-list_results_tr')

# Create empty list to store scraped content
register_list = []

# While looping over table rows, loop over content in columns, and add it to list
for tr in results:

    data = []
    for td in tr.find_all('td'):
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())

    register_list.append(data)


# Save list data to csv file
with open('Register_Service_Providers.csv', 'w', newline='', encoding="utf-8") as file:
    headers = ["Statutaire_naam", "Handelsnaam", "Vestigingsplaats"]
    write = csv.writer(file)

    write.writerow(headers)
    write.writerows(register_list)

print("Data extraction completed")
