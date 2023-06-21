import pandas as pd
import snscrape.modules.twitter as sntweet
max_tweet=50
tweet_list=[]
for t, tweet in enumerate(sntweet.TwitterSearchScraper('#Python').get_items()):
    if t >max_tweet:
        break
    else:
        tweet_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.hastags])

tweet_df=pd.DataFrame(tweet_list, columns=["Date", "Tweet ID", "Content", "Username", "Hastag"]) 
tweet_df.to_excel(r"C:\Users\asus\Masaüstü\PythonProjeleri\Twitter_DataMining\tweet_list.xlsx",
                   sep=",",
                   encoding="utf-8-sig")
 