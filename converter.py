import os
import requests
from pydub import AudioSegment

desiredfolder = 'C:\\Users\\joeld\\Desktop\\Python\\ebird\\sounds\\'
desiredfolderimg = 'C:\\Users\\joeld\\Desktop\\Python\\ebird\\img\\'
#desiredfolder = 'D:\\ebirdsounds\\sounds\\'
#desiredfolderimg = 'D:\\ebirdsounds\\img\\'


def cut(name):
    path = desiredfolder+name
    try:
        sound = AudioSegment.from_file(file = desiredfolder+"raw\\"+name+'.wav', format = 'mp3')
        
        newsound = sound[5*1000:35*1000]
        newsound.export(path+'.mp3',format = "mp3")
    except:
        print('error! '+path)

def downloadbirdsound(soundid,name):
    link = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{soundid}/audio'
    req = requests.get(link)
        
    f = open(desiredfolder+"raw\\"+name+'.wav','wb')
    f.write(req.content)
    f.close()
    req.close()

    cut(name)

def downloadbirdimage(imgid,name):
    link = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{imgid}'
    req = requests.get(link)
    f = open(desiredfolderimg+name+'.jpg','wb')
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

def newgetsoundfrombird(birdid,count):
    link = f"https://ebird.org/species/{birdid}"
    req = requests.get(link)
    txt=req.text
    req.close()

    soundids = []

    for x in range(count):
        find = txt.find('https://macaulaylibrary.org/audio/')
        if find == -1:
            break
        
        txt=txt[find+34:]
        soundids.append(txt[:txt.find('\"')])

    return soundids
    

def getimgfrombird(birdid,name):
    link = f"https://ebird.org/species/{birdid}"
    req = requests.get(link)
    txt=req.text
    req.close()
    txt=txt[txt.find('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/')+56:]
    txt=txt[:txt.find('/')]
    downloadbirdimage(txt,name)
    

f = open('species.txt','r')
txt=f.read()
f.close()

soundstodownload=[x.split(';') for x in txt.split('\n')]

for i,x in enumerate(soundstodownload):
    print(f'downloading: {x[0]} {i}/{ len(soundstodownload) } {int( i/len(soundstodownload)*100 )}%')
    downloadmultipleids(newgetsoundfrombird(x[1],10),x[0])

for x in soundstodownload:
    getimgfrombird(x[1],x[0])
