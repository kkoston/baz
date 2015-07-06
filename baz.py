import requests
import re
from bs4 import BeautifulSoup

r = requests.get('http://bazarynka.com/ogloszenia/kategoria/10/lokal-do-wynajecia/strona/1')

soup = BeautifulSoup(r.text, 'lxml')
ads = soup.find_all('ul', id=re.compile('id\d+'))

for ad in ads:
    ad_id = ad.attrs['id'].replace('id', '')
    adt = ad.getText()
    adt = re.sub(r'\s+', ' ', adt).replace('Lokal do Wynajecia', '').strip()
    if not adt[0].isdigit():
        continue
        
    date = adt[:10]
    adt = adt[13:]
    
    price = ''
    price = re.search(r'cena \$: (\d+)', adt)
    if price != None:
        price = price.group(1)
    
    name = ''    
    name = re.search(r'name: ([^\s]+)', adt)
    if name != None:
        name = name.group(1)        
    
    adt = re.sub(r'<more>.*', '', adt)    
    
    if adt[:90].find(' - ') != -1:
        adts = adt.split(' - ')
        location = adts[0]
        adt = adts[1]
    else:
        location = ''
    phone = 'http://bazarynka.com/ogloszenia/telefon/%s/ktory/1' % ad_id
    
    title = adt[:100]
    
    print "%s\n%s $%s" % (title, location, price)
    print



