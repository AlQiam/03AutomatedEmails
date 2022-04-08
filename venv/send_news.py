# We don't need classes for ExcelFile and Email as we'll use
# third party ready-to-use libraries such as Pandas, Premailer, and Yagmail

from newsapi import NewsApiClient

class NewsFeed:
    """Representing multiple news titles and links as a single string"""

    def __init__(self, interest, from_date, to_date, language,
                 api_key='76892424d8734481bb43b586fe59ae0c'):
        self.api_key = api_key
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        all_articles = self._get_articles_()

        email_body = ""
        articles = all_articles['articles']
        for article in articles:
            email_body += f"Title: {article['title']}\n" + \
                          f"Link: {article['url']}\n" \
                          + f"Published at: {article['publishedAt'].split('T')[0]}\n"\
                          + '___________\n'
        email_body += f"Number of news: {len(articles)}"
        return email_body

    def _get_articles_(self):
        newsapi = NewsApiClient(api_key=self.api_key)
        all_articles = newsapi.get_everything(qintitle=self.interest,
                                              language=self.language,
                                              from_param=self.from_date,
                                              to=self.to_date)
        return all_articles


if __name__ == "__main__":
    nf = NewsFeed('LeBron James', '2022-03-26', '2022-03-28', 'en')
    print(nf.get())
