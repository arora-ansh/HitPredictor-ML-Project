from lyrics_extractor import SongLyrics
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("../datasets/spotify_music.csv")
m = data.shape[0]

f = open("../datasets/lyrics.csv",'a')
writer = csv.writer(f)

# JSON API KEY from https://developers.google.com/custom-search/v1/overview Search Engine ID from https://cse.google.com/cse/create/new, website to search mei https://genius.com/
# pass the GCS_API_KEY = AIzaSyAyrJ0ljh-58kXH0YX1eXo_DEdWR5axgqA, GCS_ENGINE_ID = 286d7776a1820cb5c
# Tushar API key =  AIzaSyBJcu294CLp0MNFmNDmNHh35t4-qTjcuxU , GCS_ENGINE_ID = 7c91ebb5c3c3002e6
extract_lyrics = SongLyrics("AIzaSyAyrJ0ljh-58kXH0YX1eXo_DEdWR5axgqA","286d7776a1820cb5c") ## Ansh
# extract_lyrics = SongLyrics("AIzaSyBJcu294CLp0MNFmNDmNHh35t4-qTjcuxU","7c91ebb5c3c3002e6") ## Tushar
i = 0
df = pd.read_csv('../datasets/lyrics.csv')

for j in range(df.shape[0], m):
    t = data.iloc[j]["Track"] + " " + data.iloc[j]["Artist"]
    print(t,end = "\r")
    # print(extract_lyrics.get_lyrics(t))
    try:
        writer.writerow([data.iloc[j]['Id'], t, extract_lyrics.get_lyrics(t)['lyrics']])
    except Exception as e:
        e = eval(str(e))
        if(e['error']=='No results found'):
            writer.writerow([data.iloc[j]['Id'], t, 'NA'])
            continue
        writer.writerow([data.iloc[j]['Id'], t, extract_lyrics.get_lyrics(t)['lyrics']])
