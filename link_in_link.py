from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter Position: '))
i = 0
while i < count:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    lst = []
    for tag in tags:
        x = tag.get('href', None)
        lst.append(x)
    url = lst[pos-1]
    i = i + 1
name = re.findall('.+_(.+).html',url)
print(name)
