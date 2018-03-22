from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='dea79ec85f334879a9e9c59e5077bece')
top_headlines = newsapi.get_top_headlines(
                                          category='cricket',
                                          language='en',
                                          country='in'
                                          )
print(top_headlines)