from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.oysterbath.com/store-locator').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('oysterbath_dealers.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dealer Name', 'Owner Name', 'Address', 'City', 'PostCode','Website', 'logo', 'Contact', 'email', 'dir'])

dealers = soup.find_all('div', class_='list-content')

for dealer in dealers:
    print(dealer)
    print() 
    data = []
    for attr in dealer.find_all('div'):
        data.append(attr.text)
        
    csv_writer.writerow(data)

csv_file.close()

print("DONE")