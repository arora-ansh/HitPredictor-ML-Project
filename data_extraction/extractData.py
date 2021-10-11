import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd
import time
import numpy as np
import csv
import time
start_time = time.time()
sleep_min = 2
sleep_max = 5
file = open('spotify2.csv')
type(file)
csvreader = csv.reader(file)


client_id = "3ea50e2d2e3e49adbda3213a28140fb0"
client_secret = "602bf3254c4f4bc2978bb5aaec451e9b"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
spotify_url = {}
def audio_features(id):

    features = sp.audio_features(id)

    spotify_url[id[0]]['acousticness']=(features[0]['acousticness'])
    spotify_url[id[0]]['danceability']=(features[0]['danceability'])
    spotify_url[id[0]]['energy']=(features[0]['energy'])
    spotify_url[id[0]]['instrumentalness']=(features[0]['instrumentalness'])
    spotify_url[id[0]]['liveness']=(features[0]['liveness'])
    spotify_url[id[0]]['loudness']=(features[0]['loudness'])
    spotify_url[id[0]]['speechiness']=(features[0]['speechiness'])
    spotify_url[id[0]]['tempo']=(features[0]['tempo'])
    spotify_url[id[0]]['key']=(features[0]['key'])
    spotify_url[id[0]]['mode']=(features[0]['mode'])
    spotify_url[id[0]]['speechiness']=(features[0]['speechiness'])
    spotify_url[id[0]]['valence']=(features[0]['valence'])

cnt = 0
df = pd.read_csv('spotify.csv')

def write(spotify_url):
    dic_df = {}
    dic_df['id'] = []
    dic_df['Rank'] = []
    dic_df['Track'] = []
    dic_df['Artist'] = []
    dic_df['Streams'] = []
    dic_df['Week'] = []
    dic_df['Album_Name'] = []
    dic_df['Explicit'] = []
    dic_df['Track_Number_on_Album'] = []
    dic_df['Artist_Followers'] = []
    dic_df['Artist_Genres'] = []
    dic_df['acousticness'] = []
    dic_df['danceability'] = []
    dic_df['energy'] = []
    dic_df['instrumentalness'] = []
    dic_df['liveness'] = []
    dic_df['loudness'] = []
    dic_df['speechiness'] = []
    dic_df['tempo'] = []
    dic_df['mode'] = []
    dic_df['key'] = []
    dic_df['valence'] = []
    features = []
    for k in dic_df.keys():
        features.append(k)
    features.remove('id')
    for track in spotify_url.keys(): 
        for feature in features:
            # print(dic_df[feature],spotify_url[track][feature])
            dic_df[feature].append(spotify_url[track][feature])
        # print(track)
        dic_df['id'].append(track)
            
    # len(dic_df['album'])
    dataframe = pd.DataFrame.from_dict(dic_df)
    # # final_df = dataframe.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()
    dataframe.to_csv("spotify_music.csv",index=False)

for ind in df.index:
    id = [df['Link'][ind]]
    cnt = cnt + 1
    if(cnt % 100 == 0): 
        write(spotify_url)
        print(str(cnt) + " tracks completed")
        print('Loop #: {}'.format(cnt))
        print('Elapsed Time: {} seconds'.format(time.time() - start_time))
    # if(cnt % 1000 == 0):
    if id[0] in spotify_url.keys():
        if(spotify_url[id[0]]['Rank'] <= df['Rank'][ind]):
            continue
    spotify_url[id[0]] = {}
    spotify_url[id[0]]['Rank']=df['Rank'][ind]
    spotify_url[id[0]]['Track']=df['Track'][ind]
    spotify_url[id[0]]['Artist']=df['Artist'][ind]
    spotify_url[id[0]]['Streams']=df['Streams'][ind]
    spotify_url[id[0]]['Week']=df['Week'][ind]
    spotify_url[id[0]]['Album_Name']=df['Album_Name'][ind]
    spotify_url[id[0]]['Duration_MS']=df['Duration_MS'][ind]
    spotify_url[id[0]]['Explicit']=1 if (df['Explicit'][ind]) else 0
    spotify_url[id[0]]['Track_Number_on_Album']=df['Track_Number_on_Album'][ind]
    spotify_url[id[0]]['Artist_Followers']=df['Artist_Followers'][ind]
    spotify_url[id[0]]['Artist_Genres']=df['Artist_Genres'][ind]
    try:
        audio_features(id)
    except:
        print("Rate limit reached! waiting...")
        time.sleep(15)
        audio_features(id)
        print(str(cnt) + " tracks completed")
        print('Elapsed Time: {} seconds'.format(time.time() - start_time))
# print(spotify_url)