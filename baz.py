import requests
import re
from bs4 import BeautifulSoup

r = requests.get('http://bazarynka.com/ogloszenia/kategoria/10/lokal-do-wynajecia/strona/1')

soup = BeautifulSoup(r.text, 'lxml')
ads = soup.find_all('ul', id=re.compile('id\d+'))

for ad in ads:
    print ad.attrs['id']
    adt = ad.getText()
    adt = re.sub(r'\s+', ' ', adt).replace('Lokal do Wynajecia', '').replace(' - ', '\n').strip()
    if not adt[0].isdigit():
        continue
    print adt
    print


