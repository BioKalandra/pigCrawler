
from urllib.request import urlopen as req
url = 'https://unsplash.com/s/photos/landscape'

try:
    request = req(url)
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :( ', exception)
pageHtml = request.read()

