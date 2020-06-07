import requests as req  # to get image from the web
import shutil # to save it locally
import math, os, sys

filename = 'assets/piclist.txt'
foldername = 'testpics'

file = open(filename, 'r')
images = []

for line in file:
    img = file.readline()
    images.append(img)

try:
    os.mkdir('assets/' + foldername)
    print('ordner erstellt')
except Exception as exc:
    print('Fehler beim Erstellen des Ordners(schon vorhanden??)')
    print('Abbruch :(')
    sys.exit()

amount = len(images)
print('es werden ' + str(amount) + ' images geladen')

counter = 0
for img in images:
    progress = math.trunc((counter / amount) * 100)
    progress = str(progress) + '%'
    print('progress: ' + progress) 

    try:
        r = req.get(img, stream="true")
        if r.status_code != 200:
            raise Exception('Fehler beim Aufbauen der Verbindung')
        r.raw.decode_content = True
        with open('assets/' + foldername + '/pic_' + str(counter) + '.jpeg', 'wb') as file:
            shutil.copyfileobj(r.raw, file)
    except Exception as exception:
        print(exception)

    counter = counter + 1
