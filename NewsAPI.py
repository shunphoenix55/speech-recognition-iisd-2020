#NewsAPI
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='d3015796d52f42d2b36cf0d61fbe7a0c')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          #sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2020-11-04',
                                      to='2020-12-01',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()
articles = top_headlines["articles"]
#for i in articles:
 #   print(i["title"])
#print(articles)

top_news = newsapi.get_top_headlines()
#for i in range (0, 5):
 #   print(top_news["articles"][i]["title"])
  #  print(top_news["articles"][i]["description"])

def get_news(user_speech):
    if "news" in user_speech.lower():
        top_news = newsapi.get_top_headlines()
        news_str = ""
        for i in range (0, 5):
            news_str += top_news["articles"][i]["title"] + "\n"
            news_str += top_news["articles"][i]["description"] + "\n"
        return news_str

user_speech = input("Enter user input: ")
print(get_news(user_speech))
