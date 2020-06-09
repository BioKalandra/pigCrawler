from urllib.request import urlopen as req
import requests as reqPic  # to get image from the web
from bs4 import BeautifulSoup as soup
import shutil # to save it locally
import re, os, sys

category = 'landscape'
url = 'https://unsplash.com/s/photos/' + category
foldername = category
quality = 7 #1-7
regex = r'(?<=' + str(quality) + '00w,\s)https:\/\/images.unsplash.com\/photo.*w=' + str(quality+1) + '00&q=60(?=\s' + str(quality+1) + '00w)'
regex = r'(?<=300w,\s)https:\/\/images.unsplash.com\/photo.*w=400&q=60(?=\s400w)'

try:
    request = req(url)
    pageHtml = request.read()
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :( ', exception)

links = []
sFile = soup(pageHtml, "html.parser")

try:
    imagesUncut = sFile.select('a > div > img')
    amount = len(imagesUncut)
    print('Es gibt ' + str(amount) + ' images')
except Exception as exception:
    print('Fehler beim Soupen ...\n', exception)

images=[]


for img in imagesUncut:
    picUrl = img.get('srcset')
    images.append(picUrl)

try:
    folder = 'assets/' + foldername
    if(os.path.exists(folder)) :
        shutil.rmtree(folder, ignore_errors='true')
        print('alter ordner gelöscht')
    os.mkdir(folder)
except FileExistsError as exc:
    print('Fehler beim Erstellen/Löschen des Ordners')
    sys.exit()

counter = 1
for img in images:
    try:
        m = re.search(regex, img)
        m.group(0)
        print(m.group(0))
        # print(img)
        r = reqPic.get(img, stream="true")
        if r.status_code != 200:
            raise Exception('Fehler beim Aufbauen der Verbindung')
        r.raw.decode_content = True
        with open('assets/' + foldername + '/pic_' + str(counter) + '.jpeg', 'wb') as file:
            shutil.copyfileobj(r.raw, file)
        counter = counter + 1
        progress = ((counter*100)/amount)
        display = str(round(progress, 2))
        print('downloading: ' + display + '%')
    except Exception as exception:
        print(exception)