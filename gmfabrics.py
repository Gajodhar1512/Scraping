import requests
import csv, re
from bs4 import BeautifulSoup

url = "https://gmfabrics.com/storelocator?&page="

csv_file = open('gmfabrics.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Address'])

for state in range(1, 17):
    print(state)
    source = requests.get(url+str(state)).text
    soup = BeautifulSoup(source, 'lxml')
    dealers = soup.find_all('div', class_='storenameadd')
    for dealer in dealers:
        name = dealer.find('h3').text
        print("  " + name)
        address = dealer.find('p').text
        csv_writer.writerow([name, address])

csv_file.close()
print("Done")