import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    filtered_tweets = tweets[tweets['content'].str.len() < 15]
    result = filtered_tweets[['tweet_id', 'content']]
    return result


data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})
print(invalid_tweets(tweets))
