from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://royalebathrooms.com/stores/stores_listing').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('royalebathrooms_dealers.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dealer Name', 'Address', 'City', 'Phone'])

dealers = soup.find('div', id='append_form').find_all('li')


for dealer in dealers:
    name = dealer.find('h5').text
    dealer = dealer.find('p').text.replace(' ', '')
    dealer = dealer.replace('\r', ' ')
    dealer = dealer.replace('\n', ' ')
    address = dealer.split()[0]
    city = dealer.split()[1]
    phone = dealer.split()[2][13:]
   
    csv_writer.writerow([name, address, city, phone])

csv_file.close()

print("DONE")