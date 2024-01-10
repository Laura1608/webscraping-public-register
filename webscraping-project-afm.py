import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

url = 'https://www.afm.nl/nl-nl/sector/registers/vergunningenregisters/financiele-dienstverleners/details?id=C18B1D63-774C-E811-80D9-005056BB0C82'

# Create dictionary with user-agent = Firefox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}

# Retrieve content from webpage
response = requests.get(url, headers=headers)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# Create empty list to store scraped content with company info
company_info = []

while True:
    # Loop over table content based on tag
    for item in soup.select(".cc-mobile-title"):
        item.extract()

        # Convert the data to a pandas dataframe
        data = pd.read_html(StringIO(str(soup)))[0]

    # Loop over list content, and select its labels and values
    for label, value in zip(
        soup.select(".cc-em--detail-list__label"),
        soup.select(".cc-em--detail-list__value"),
    ):
        # Get the text from each label and value, and add them to dataframe
        data[label.get_text(strip=True)] = value.get_text(strip=True)

    company_info.append(data)

    # Find URL of next page by automatically selecting element
    next_url = soup.select_one('a:-soup-contains("Volgende register resultaat")')
    if not next_url:
        break
    url = "https://www.afm.nl/" + next_url["href"]

# Concatenate to one dataframe and save as csv
register = pd.concat(company_info)
register.to_csv('Register_AFM.csv', index=False)
print('Company info received!')
