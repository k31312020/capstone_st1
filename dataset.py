import pandas as pd

most_subscribed_channels = pd.read_csv('most_subscribed_youtube_channels.csv')

RANK_COL = 'rank'
VIEWS_COL = 'video views'
VIDEOS_COL = 'video count'
CATEGORY_COL = 'category'
SUBSCRIBERS_COL = 'subscribers'
STARTED_COL = 'started'