import yagmail
import pandas as pd
from send_news import NewsFeed
import datetime
import time


def email_news():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday.strftime('%Y-%m-%d'),
                         to_date=today.strftime('%Y-%m-%d'),
                         language='en')
    sender.send(to=row['email'],
                subject=f'Your {row["interest"]} news for today!',
                contents=f"Hi {row['name']},\nSee what's on about {row['interest']} today!\n\n{news_feed.get()}", )


while True:
    if datetime.datetime.now().hour == 12 and \
            datetime.datetime.now().minute == 19:
        emails = pd.read_excel('people.xlsx')
        sender = yagmail.SMTP(user='QiamPython@gmail.com', password='devtech?1')
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=1)
        print("Executing Finally!")
        for index, row in emails.iterrows():
            email_news()

    time.sleep(60)
