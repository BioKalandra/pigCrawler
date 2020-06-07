from bs4 import BeautifulSoup as soup

try:
    file = open('assets/index.html', 'rb')
    data=file.read()
except Exception as exception:
    print('Fehler :(', exception)

soup = soup(data, "html.parser")

links=[]

try:
    imagesUncut = soup.select('img[data-large-src]')
    print('es gibt ' + str(len(imagesUncut)) + ' images')
except Exception as exception:
    print('Fehler beim Soupen ...\n', exception)

images=[]

counter = 1
for img in imagesUncut:
    image_with_parameters = img.get('data-large-src')
    indexCutOff = image_with_parameters.find('.jpeg')+5
    if (indexCutOff < 5):
        continue
    image = image_with_parameters[0 : indexCutOff]
    images.append(image)
    print(str(counter) + ' -> ' + image)
    counter = counter +1

# for img in images:
#      links.append(img['src'])

# for l in links:
#      print(l)