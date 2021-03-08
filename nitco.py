from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://viterotiles.com/find-a-store/').text
soup = BeautifulSoup(source, 'lxml')
dealers = soup.find_all('div', class_='mylocBox')

csv_file = open('viterotiles.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Address', 'Phone'])

for dealer in dealers:
    print(dealer)
    print()
    name = dealer.find('h3').text
    phone_string = str(dealer.find('p').contents[-2])
    phone = phone_string.replace('Phone No.', "").strip().replace(' ','')
    if phone.isalnum():
        dealer.find('p').contents.pop(-2)
        address = dealer.find('p').text.replace(phone_string, "")
    else:
        phone = ""
        address = dealer.find('p').text

    csv_writer.writerow([name, address, phone])

csv_file.close()

print("DONE")