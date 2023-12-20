import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://github.com/'  # Replace with the actual URL you want to scrape

# Make an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and print the title of the page
    title = soup.title.string
    print(f"Title: {title}\n")

    # Find and print all the links on the page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            print(f"Link: {href}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")