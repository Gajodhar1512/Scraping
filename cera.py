import requests
import csv, re
from bs4 import BeautifulSoup

url = "https://www.cera-india.com/tiles-dealer/?locatorType=&locatorState="

csv_file = open('cera_tiles_dealers.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Address', 'Phone', 'Email'])

for state in range(1, 37):
    source = requests.get(url+str(state)).text
    soup = BeautifulSoup(source, 'lxml')
    dealers = soup.find('div',class_='cnt_addrs_wrp').find_all('li')
    print(state)
    if len(dealers) == 0:
        continue
    for dealer in dealers:
        print(dealer)
        print()        
        name = dealer.find('h3').text
        address = dealer.find('div',class_='cnt_add').text
        try:
            phone = dealer.find('div',class_='cnt_no').text
        except:
            phone = ""
        try:
            email = dealer.find('div',class_='cnt_mail').text
        except:
            email = ""
        csv_writer.writerow([name, address, phone, email])

csv_file.close()
print("Done")