from bs4 import *
import requests
import os 

# from urllib.request import urlopen as uReq
# url = 'https://www.heise.de/'
# request = uReq(url)
# pageHtml = request.read()

# headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#             'Accept-Encoding': 'none',
#             'Accept-Language': 'en-US,en;q=0.8',
#             'Connection': 'keep-alive'
#             }

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

#url = "https://pypi.org/project/beautifulsoup4/"
url = "https://www.pexels.com/@hiteshchoudhary"

response = requests.get(url, stream = True, headers=headers)
print(response)
soup2 = BeautifulSoup(response.text, "html.parser")

links=[]

images = soup2.select('img[src^="https://images.pexels.com/photos]')

for img in images:
    links.append(img['src'])

for l in links:
    print(l)