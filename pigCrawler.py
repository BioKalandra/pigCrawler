#zum testen -> 600w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=700&amp;q=60 700w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=60 800w, https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=900&amp;q=60

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import re

url = 'https://unsplash.com/s/photos/landscape'
regex = '(?<=700w,\s)https:\/\/images\.unsplash\.com\/photo.*(?=\s800w,\s)'

try:
    request = req(url)
    print('erfolgreich geladen')
except Exception as exception:
    print('Fehler :( ', exception)
pageHtml = request.read()

links = []
soup = soup(pageHtml, "html.parser")

try:
    imagesUncut = soup.select('img[srcset]')
    print('es gibt ' + str(len(imagesUncut)) + ' images')
except Exception as exception:
    print('Fehler beim Soupen ...\n', exception)

images=[]

counter = 1
for img in imagesUncut:
    many_pics_string = img.get('src')
    
    image = re.search(regex, many_pics_string)
    print(image.group())
    images.append(image[0])
    print(str(counter) + ' -> ' + image.group())
    counter = counter +1
