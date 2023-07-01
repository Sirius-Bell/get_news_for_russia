from newsapi import NewsApiClient


class GetNews:
	"""
	News for country
	"""
	def __init__(self, api_key: str, language: str = "ru") -> None:
		if api_key is None: raise ValueError
		self.api_key = api_key
		self.api = NewsApiClient(api_key=self.api_key)
		self.language = language

	def getNews(self) -> dict:
		"""
		Get news in specific country
		:return: article news
		"""
		top_headlines = self.api.get_top_headlines(country=self.language, language=self.language)
		for i in top_headlines['articles']: yield i


if __name__ == "__main__":
	news = GetNews(api_key=None, language='ru')
	print(news.getNews())
