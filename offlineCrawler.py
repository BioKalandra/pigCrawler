from bs4 import *
import os, random, requests

try:
    file = open('assets/landscape.html', 'rb')
    data=file.read()
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :(', exception)

soup = BeautifulSoup(data, "html.parser")

links=[]

try:
    # images = soup.select('img[src^="https//images.pexels.com/photos"]')
    # images = soup.select('img[src]')
    imagesUncut = soup.select('img[data-large-src]')
    print('done')

    print('es gibt ' + str(len(imagesUncut)) + ' images')
except Exception as exception:
    print('Fehler beim Soupen ...\n', exception)

images=[]

for img in imagesUncut:
    print(img)
    print(img.find('.jpeg'))

for img in images:
     links.append(img['src'])

for l in links:
     print(l)