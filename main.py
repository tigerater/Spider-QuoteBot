#Spider-man test bot for reddit @tigerater https://www.reddit.com/user/tigerater
#implemented at https://www.reddit.com/user/spider-manbot
#github https://github.com/tigerater/Spider-Man-Bot
#email tigerater@gmail.com, don't hesitate to ask me anything!

#!/usr/bin/python
import praw
import pdb
import re
import os
import pickle

reddit = praw.Reddit('bot2')

#this checks to see firstly if the comment starts with a quote (and then ignores it) and thereafter if spiderman is in the text without a hyphen
def checkcondition(c):
    text = c.body
    if text[0] != '>':
        if "spiderman" in text or "Spiderman" in text:
            return True
        else:
            return False

#lakes the last 500 comments posted in the subreddit marvelstudios at the time of searching
#comments = reddit.inbox.mentions(limit = 50)


#checks to see if the comment has already been replied to
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))
"""
#counter to see how many times we've been called- also uses the num2words module to convert ints to ordinals.
def checkcounter():
    with open("counter.txt", "r") as f:
        counter = int(f.read())
        counter += 1
    with open("counter.txt", "w") as g:
        g.write(str(counter))
        return(num2words(counter, to='ordinal'))
"""
with open("Spiderman1FULL.txt", "rb") as fp:
    final = pickle.load(fp)

subreddit = reddit.subreddit('raimimemes')
comments = subreddit.comments(limit = 500)

for comment in comments:
    if comment.id not in comments_replied_to:
        text = comment.body
        if 'u/spider-quotebot' in text.lower():
            position = [int(s) for s in text.split() if s.isdigit()]
            if len(position):
                if position[0] <= len(final) and position[0] >= 0:
                    result = final[position[0]-1][1].replace("<i>","*")
                    result2 = result.replace("</i>","*")
                    comment.reply(result2 + "\n\n *Hello! I'm a bot and this action was performed automatically. A message in the format *number myusername* will let me reply with that numbered line from Spider-Man(2002))")
                    comments_replied_to.append(comment.id)
    with open("comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")











        
