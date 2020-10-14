from bs4 import BeautifulSoup
import requests
import csv

item_slots = [
    'amulets', 'axes', 'belts', 'body_armours', 'boots', 'bows',
    'caster_daggers', 'caster_staves', 'claws', 'daggers', 'generic_daggers',
    'generic_staves', 'gloves', 'helmets', 'maces', 'quivers', 'rings',
    'rune_daggers', 'sceptres', 'shields', 'staves', 'swords',
    'thrusting_one_hand_swords', 'wands', 'warstaves'
]

url = 'https://pathofexile.gamepedia.com/List_of_'
filename = 'ItemBases.csv'

with open(filename, 'w') as myfile:
    for itemSlot in item_slots:
        print('Currently retreiving data for: ' + itemSlot)
        r = requests.get(url + itemSlot)
        soup = BeautifulSoup(r.content, 'html.parser')
        tables = soup.find('table')

        base_names = []
        base_names.append(itemSlot)
        for row in tables.find_all('tr'):
            links = row.find('a', href=True)
            try:
                title = links.attrs['title']
                base_names.append(title)

            except AttributeError:
                pass

        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(base_names)
print('Sucessfully downloaded data, file saved as: ' + filename)
