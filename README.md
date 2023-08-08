# Lehrhaus Mastodon Bot
A Mastodon bot which pulls from the public RSS feed from [The Lehrhaus](https://thelehrhaus.com/) and posts to Mastodon whenever a new article is added to the RSS feed.

The `toot.py` script must be manually run in order to check the RSS feed and post if a new article is found. This process can be automated using a cronjob or similar method.

The code should be able to be adapted fairly easily to other websites with a public RSS feed.
