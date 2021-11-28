from lyrics_extractor import SongLyrics
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("../datasets/spotify_music.csv")
m = data.shape[0]

f = open("../datasets/lyrics.csv",'a')
writer = csv.writer(f)

# JSON API KEY from https://developers.google.com/custom-search/v1/overview Search Engine ID from https://cse.google.com/cse/create/new, website to search mei https://genius.com/
# pass the GCS_API_KEY = classified, GCS_ENGINE_ID = classified

extract_lyrics = SongLyrics("classfied","classified") 
i = 0
df = pd.read_csv('../datasets/lyrics.csv')

for j in range(df.shape[0], m):
    t = f'{data.iloc[j]["Track"]} {data.iloc[j]["Artist"]}'
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
