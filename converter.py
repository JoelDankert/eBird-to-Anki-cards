import webbrowser
import time
import os
import requests

downloadfolder = 'D:\\Downloads\\'
desiredfolder = 'D:\\ebirdsounds\\'


def downloadbirdsound(soundid,name):
    webbrowser.open(f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{soundid}/audio')
    time.sleep(3)
    os.rename(downloadfolder+"audio",desiredfolder + name + '.wav')

def downloadmultipleids(ids,names):
    for n,idc in enumerate(ids):
        downloadbirdsound(idc,names[idc])


def getsoundfrombird(birdid, soundname)
    link = 'https://media.ebird.org/catalog?taxonCode={birdid}&mediaType=audio&tag=song&sort=rating_rank_desc&regionCode=DE'
    req = requests.get(link)
