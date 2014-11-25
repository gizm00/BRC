#scraper
import feedparser
from bs4 import BeautifulSoup, NavigableString
import urllib2
import re
from phrase_phinder import PhrasePhinder

invalid_tags = ['href', 'b']

def GetText(feed) :
    text = BeautifulSoup(fd).get_text()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    text = filter(lambda x: not re.match(r'^\n', x), text)
    return text

## These tuples will be part of the user admin
feeds = ['http://www.huffingtonpost.com/feeds/verticals/divorce/index.xml',
         'http://www.huffingtonpost.com/feeds/verticals/black-voices/index.xml',
         'http://www.npr.org/rss/rss.php?id=1057',
         'https://medium.com/feed/surviving-the-future',
         'http://rss.cnn.com/rss/money_latest.rss']
         
phrasePhinder = PhrasePhinder()

# populates lists
title = []
link = []
summary = []
for feed in feeds:
    a = feedparser.parse(feed)
    title += [i.title for i in a.entries]
    link += [i.link for i in a.entries]
    summary += [i.description for i in a.entries]

    fd = urllib2.urlopen(feed)
    text = GetText(fd)
    phrases = phrasePhinder.AnalyzeText(text)
    print phrases
    print 
    print

# populates database

