from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://glocera.com/dealer_location').text

soup = BeautifulSoup(source, 'lxml')

# csv_file = open('glocera_dealers.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Dealer Name', 'Owner Name', 'Address', 'City', 'PostCode','Website', 'logo', 'Contact', 'email', 'dir'])

dealers = soup.find_all('div', class_='left-details')
import pdb; pdb.set_trace()

# for dealer in dealers:
#     print(dealer)
#     print() 
#     data = []
#     for attr in dealer.find_all('div'):
#         data.append(attr.text)
        
#     csv_writer.writerow(data)

# csv_file.close()

print("DONE")