import requests

api_key = "66a8f5f3015e47b7b8f48e7ac08ec46f"
url = f"https://newsapi.org/v2/top-headlines?category=technology&country=us&apiKey={api_key}"
response = requests.get(url)
data = response.json()
print(data)
