import os
import requests

desiredfolder = 'C:\\Users\\joeld\\Desktop\\Python\\ebird\\sounds\\'


def downloadbirdsound(soundid,name):
    link = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{soundid}/audio'
    req = requests.get(link)
    f = open(desiredfolder+name+'.wav','wb')
    f.write(req.content)
    f.close()
    req.close()

def downloadmultipleids(ids,name):
    #if not os.path.exists(desiredfolder+name):
    #    os.mkdir(desiredfolder+name)
        
    for i,idc in enumerate(ids):
        downloadbirdsound(idc,f'{name}_{i+1}')

#def getratings(assetid):
#    checker = requests.get(f'https://macaulaylibrary.org/asset/{name}')
#    checkertext = checker.text
#    checkertext = checkertext[checkertext.find('RatingStars-count\">'):]
#    ratings = checkertext[:checkcertext.find(' ratings')]
#    return int(ratings)

def getsoundfrombird(birdid,count):
    link = f'https://media.ebird.org/catalog?taxonCode={birdid}&mediaType=audio&sort=rating_rank_desc&regionCode=DE'
    req = requests.get(link)
    txt=req.text
    req.close()
    soundids = []

    while len(soundids) < count:
        try:
            txt=txt[txt.find('assetId')+8:]
            name = txt[:txt.find(',')]
            
            #rat = getratings(name)
            #if (rat > 10):
            soundids.append(name)
            
        except:
            print(f'ERROR: failed to collect sound: {birdid}: {len(soundbirds)}')
    
    return soundids

f = open('species.txt','r')
txt=f.read()
f.close()

soundstodownload=[x.split(';') for x in txt.split('\n')]


for x in soundstodownload:
    downloadmultipleids(getsoundfrombird(x[1],3),x[0])

