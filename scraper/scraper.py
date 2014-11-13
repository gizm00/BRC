import feedparser

## These tuples will be part of the user admin
feeds = ['http://www.huffingtonpost.com/feeds/verticals/divorce/index.xml',
         'http://www.huffingtonpost.com/feeds/verticals/black-voices/index.xml',
         'http://www.npr.org/rss/rss.php?id=1057',
         'https://medium.com/feed/surviving-the-future',
         'http://rss.cnn.com/rss/money_latest.rss']

# populates lists
title = []
link = []
summary = []
for feed in feeds:
    a = feedparser.parse(feed)
    title += [i.title for i in a.entries]
    link += [i.link for i in a.entries]
    summary += [i.description for i in a.entries]

# populates database

