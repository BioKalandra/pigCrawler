#zum testen -> 600w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=700&amp;q=60 700w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=60 800w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=900&amp;q=60

from urllib.request import urlopen as req
import requests as reqPic  # to get image from the web
from bs4 import BeautifulSoup as soup
import shutil # to save it locally
import re, os, sys

category = 'landscape'
url = 'https://unsplash.com/s/photos/' + category
url = 'https://www.heise.de/'
foldername = 'heise'
regex = '(?<=700w,\s)https:\/\/images\.unsplash\.com\/photo.*(?=\s800w,\s)'

try:
    request = req(url)
    pageHtml = request.read()
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :( ', exception)

links = []
sFile = soup(pageHtml, "html.parser")

try:
    # imagesUncut = sFile.select('a > div > img')
    imagesUncut = sFile.select('img')
    print('es gibt ' + str(len(imagesUncut)) + ' images')
except Exception as exception:
    print('Fehler beim Soupen ...\n', exception)

images=[]


for img in imagesUncut:
    # many_pics_string = img.get('src')
    picUrl = img.get('src')
    
    # image = re.search(regex, many_pics_string)
    # print(image.group())
    images.append(picUrl)

# try:
#     os.mkdir('assets/' + foldername)
#     print('ordner erstellt')
# except Exception as exc:
#     print('Fehler beim Erstellen des Ordners(schon vorhanden??)')
#     print('Abbruch :(')
#     sys.exit()

counter = 1
for img in images:
    try:
        if not img.startswith('https://'):
            continue 
        r = reqPic.get(img, stream="true")
        if r.status_code != 200:
            raise Exception('Fehler beim Aufbauen der Verbindung')
        r.raw.decode_content = True
        with open('assets/' + foldername + '/pic_' + str(counter) + '.jpeg', 'wb') as file:
            shutil.copyfileobj(r.raw, file)
        counter = counter + 1
    except Exception as exception:
        print(exception)