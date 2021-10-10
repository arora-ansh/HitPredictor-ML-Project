from lyrics_extractor import SongLyrics
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("../datasets/spotify_music.csv")
# print(data.head())
m = data.shape[0]
# print(data.iloc[0]["Track"],data.iloc[0]["Artist"])

f = open("../datasets/lyrics.csv",'w')
writer = csv.writer(f)

# JSON API KEY from https://developers.google.com/custom-search/v1/overview Search Engine ID from https://cse.google.com/cse/create/new, website to search mei https://genius.com/
# pass the GCS_API_KEY = AIzaSyAyrJ0ljh-58kXH0YX1eXo_DEdWR5axgqA, GCS_ENGINE_ID = 286d7776a1820cb5c
extract_lyrics = SongLyrics("AIzaSyAyrJ0ljh-58kXH0YX1eXo_DEdWR5axgqA","286d7776a1820cb5c")
i = 0
for j in range(m):
    t = data.iloc[j]["Track"] + " " + data.iloc[j]["Artist"]
    print(t,end = "\r")
    print(extract_lyrics.get_lyrics(t))
    if(i==100):
        break
    i+=1

# print(extract_lyrics.get_lyrics("I Don’t Wanna Live Forever (Fifty Shades Darker) Taylor Swift Zayn"))