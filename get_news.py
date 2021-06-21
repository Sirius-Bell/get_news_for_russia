from newsapi import NewsApiClient

# Init api key
API_KEY = ""

# Init api_client
api = NewsApiClient(api_key=API_KEY)

# Get news in top in json
top_headlines = api.get_top_headlines(country='ru', language='ru')

#print(top_headlines)

for i in top_headlines['articles']:
	print(i)