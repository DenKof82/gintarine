import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def crawl(time_limit, source, return_format):
    start_time = time.time()
    data = []

    # Nustatyti bazinį URL
    base_url = "https://www.gintarine.lt"
    if source == 'gintarine':
        search_url = f"{base_url}/search?q=vitamin+c"

    while True:
        # Patikrinti laiko limitą
        if time.time() - start_time > time_limit:
            break

        # Atlikti užklausą į svetainę
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Išgauti produkto duomenis
        products = soup.find_all('div', class_='product')
        for product in products:
            name = product.find('h2', class_='product-name').get_text(strip=True)
            price = product.find('span', class_='price').get_text(strip=True)
            image_url = product.find('img')['src']

            data.append({
                'Pavadinimas': name,
                'Kaina': price,
                'Nuotraukos URL': base_url + image_url
            })

        # Patikrinti, ar yra kitas puslapis
        next_page = soup.find('a', {'aria-label': 'Next'})
        if next_page:
            search_url = base_url + next_page['href']
        else:
            break

    # Grąžinti duomenis nurodytu formatu
    if return_format == 'csv':
        return pd.DataFrame(data).to_csv(index=False)
    else:
        return data

# Pavyzdinis naudojimas
rezultatas = crawl(time_limit=60, source='gintarine', return_format='csv')
print(rezultatas)