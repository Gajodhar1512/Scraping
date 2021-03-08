from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.somanyceramics.com/dealer-network?p="

csv_file = open('somaneceramics_dealers.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dealer Name', 'Address', 'City', 'Pin', 'Contact Person', 'Phone1', 'Phone2', 'email'])

for p in range(1, 95):
    print("fetching page no: {}".format(p))
    source = requests.get(url+str(p)).text
    soup = BeautifulSoup(source, 'lxml')
    dealers = soup.find_all('div', class_='product-item large category1')

    for dealer in dealers:
        name = dealer.find('div',class_='panel-heading').text        
        print(name)
        
        dealer = dealer.find('p').text.replace('\t'," ").split('\n')
        # dealer = [item for item in dealer if item not in ["", " ", ",", None]]
        address = dealer[2].strip()
        city = dealer[3].strip()
        pin = dealer[4].strip()
        contact_person = dealer[5].strip()
        try:
            phone1 = dealer[7].strip()
            phone2 = dealer[9].strip()
            email = dealer[10].strip()
            csv_writer.writerow([name, address, city, pin, contact_person, phone1, phone2, email])
            continue
        except:
            try:            
                if "@" in dealer[6].strip():
                    email = dealer[6].strip()
                    phone1=""
                    phone2=""
                    csv_writer.writerow([name, address, city, pin, contact_person, phone1, phone2, email])
                    continue
            except:
                phone1=""
                phone2=""
                email=""
                csv_writer.writerow([name, address, city, pin, contact_person, phone1, phone2, email])
                continue
            # else if dealer[6].strip().isalnum():
            #     phone1 = dealer[6].strip() 


csv_file.close()

print("DONE")