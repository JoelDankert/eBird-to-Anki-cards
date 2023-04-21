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
    if not os.path.exists(desiredfolder+name):
        os.mkdir(desiredfolder+name)
        
    for i,idc in enumerate(ids):
        downloadbirdsound(idc,f'{name}\\{name}_{i+1}')


def getsoundfrombird(birdid,count,tag = 'song'):
    link = f'https://media.ebird.org/catalog?taxonCode={birdid}&mediaType=audio&tag={tag}&sort=rating_rank_desc&regionCode=DE'
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

f = open('species.txt','r')
txt=f.read()
f.close()

soundstodownload=[x.split(',') for x in txt.split('\n')]


for x in soundstodownload:
    downloadmultipleids(getsoundfrombird(x[1],int(x[2]),x[3]),x[0])
