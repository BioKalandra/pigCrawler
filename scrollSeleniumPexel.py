from urllib.request import urlopen as req
import requests as reqPic  # to get image from the web
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import shutil # to save it locally
import re, os, sys, time


category = 'landscape'
url = 'https://www.pexels.com/search/mountains/'
foldername = category
quality = 7 #1-7
regex = r'(?<=' + str(quality) + '00w,\s)https:\/\/images.unsplash.com\/photo.*w=' + str(quality+1) + '00&q=60(?=\s' + str(quality+1) + '00w)'


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    # scrolling
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    print('lastheight ist ' + str(lastHeight))
    pause = 0.3
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        print('lastheight ist ' + str(lastHeight))
        if(lastHeight > 50000):
            break
    html = driver.page_source
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :( ', exception)

links = []
sFile = soup(html, "html.parser")

try:
    imagesUncut = sFile.select('a > div > img')
    sFile.select(x)
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
        with open('assets/' + foldername + '/' + foldername + '_' + str(counter) + '.jpeg', 'wb') as file:
            shutil.copyfileobj(r.raw, file)
        progress = ((counter*100)/amount)
        display = str(round(progress, 2))
        print('downloading: ' + display + '%')
        counter = counter + 1
    except Exception as exception:
        print(exception)