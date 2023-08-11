import os
from pathlib import Path
from mastodon import Mastodon
import feedparser
from bs4 import BeautifulSoup
import pickle

dir_name = os.path.dirname(__file__)
access_token = Path(dir_name+'/access_token.txt').read_text().strip()
mastodon = Mastodon(
    access_token = access_token,
    api_base_url = 'https://kiddush.social/'
)

d = feedparser.parse('https://thelehrhaus.com/feed/')
num_entries = min(len(d.entries),10)

posted_file = dir_name+'/posted.pickle'
for x in range(num_entries-1,-1,-1):
    entry = d.entries[x]
    link = entry.link
    if os.path.isfile(posted_file):
        with open(posted_file, 'rb') as f:
            posted_list = pickle.load(f)
    else:
        posted_list = []
    if link not in posted_list:
        desc = BeautifulSoup(entry.description,'lxml').p.text
        toot = '\"'+entry.title+'\"'+' by '+entry.author+'\n\n'+desc+'\n\n'+entry.link
        mastodon.status_post(toot, visibility='public')
        posted_list.append(link)
        with open(posted_file, 'wb') as f:
            pickle.dump(posted_list, f)
