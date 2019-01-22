#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("BotPlayGroundSpam")


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []


else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))



for submission in subreddit.hot(limit=10):
    
    if submission.id not in posts_replied_to:
       
        if re.search("i love python", submission.selftext, re.IGNORECASE):
            
            title = 'obrazek'
            url = 'https://i.imgur.com/wBpvkA0.jpg'
            reddit.subreddit('BotPlayGroundSpam').submit(title, url=url)
            
            posts_replied_to.append(submission.id)


with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")