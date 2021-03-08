from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://bindalcoir.com/dealers-locator').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('bindalcoir_dealers.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['S No', 'Dealer', 'Contact Person', 'Area/State', 'Location', 'Address'])

for dealer in soup.find_all('tr')[1:]:
    print(dealer)
    print()
    if len(dealer.find_all('td')) == 0:
        continue
    data = []
    for td in dealer.find_all('td'):
        data.append(td.text)
    
    csv_writer.writerow(data)

csv_file.close()

print("DONE")