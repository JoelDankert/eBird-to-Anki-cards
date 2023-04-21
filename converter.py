import time
import os
import requests

desiredfolder = 'D:\\ebirdsounds\\'


def downloadbirdsound(soundid,name):
    link = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{soundid}/audio'
    req = requests.get(link)
    f = open(desiredfolder+name+'.wav','wb')
    f.write(req.content)
    f.close()

def downloadmultipleids(ids,name):
    for i,idc in enumerate(ids):
        downloadbirdsound(idc,f'{name}\\{name}_{i}')


def getsoundfrombird(birdid,count):
    link = f'https://media.ebird.org/catalog?taxonCode={birdid}&mediaType=audio&tag=song&sort=rating_rank_desc&regionCode=DE'
    req = requests.get(link)
    txt=req.text

    soundids = []

    while len(soundids) < count:
        try:
            txt=txt[txt.find('assetId')+8:]
            
            soundids.append(txt[:txt.find(',')])
            
        except:
            print(f'ERROR: failed to collect sound: {birdid}: {len(soundbirds)}')
    
    return soundids

downloadmultipleids(getsoundfrombird('comchi1',5),'zilpzalp')
