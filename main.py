import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://pokemondb.net/pokedex/national'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll('div', class_='infocard')
print(results)

with open('pokemon.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)

    for result in results:
        images = result.find('span', class_='img-fixed img-sprite')
        pokemon = result.find('a', class_='ent-name').text
        types = result.findAll(True, {'class':['itype grass', 'itype poison', 'itype flying', 'itype fire', 'itype water', 'itype bug', 'itype normal', 'itype electric', 'itype ground', 'itype fairy', 'itype fighting', 'itype grass', 'itype rock', 'itype psychic', 'itype steel', 'itype ice', 'itype dragon', 'itype ghost', 'itype dark']})
        alltypes = []
        for type in types:
            alltypes.append(type.text)
        image = images['data-src']
        thewriter.writerow([image] + [pokemon] + alltypes)
