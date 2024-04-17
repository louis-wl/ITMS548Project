import requests
from tabulate import tabulate

api_key = "9dd5e981e95297329892eb834c4065ad10896138c3f44c00a36ebfc9e546b98b"

url = "https://serpapi.com/search"

params = {
    "engine": "google",
    "q": "Chicago crime",
    "num": 15,
    "api_key": api_key
}

response = requests.get(url, params=params)
data = response.json()

table_data = []

for result in data['organic_results']:
    title = result['title']
    link = result['link']
    table_data.append([title, link])

print(tabulate(table_data, headers=['Title', 'URL'], tablefmt='grid'))
