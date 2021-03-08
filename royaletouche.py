import requests
import csv, re
from bs4 import BeautifulSoup

url = "https://www.royaletouche.com/DealersNetworks/select_map1.php?city_id=-"

csv_file = open('royaletouche.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Address', 'Contact Person', 'Phone1', 'Phone2', 'Phone3', 'Phone4', 'Email1', 'Email2'])

for state in range(1, 22):
    dealers = requests.get(url+str(state)).json()
    for dealer in dealers:
        print(dealer)
        print()
        soup = BeautifulSoup(dealer['address_details'], 'lxml')
        dealer_details = soup.find_all('strong')
        # import pdb; pdb.set_trace()
        name = dealer_details[0].text.strip()
        try:
            contact_person = dealer_details[1].text.strip()
        except:
            contact_person=""
        string = soup.text        
        result = re.search('{}(.*){}'.format(name, contact_person), string)
        try:
            address = result.group(1).strip()
        except:
            address = string
        contact_details = soup.find_all('a')
        print(contact_details)
        p=1
        e=1
        dealer_dict = {}
        for tag in contact_details:
            if "@" in tag.text:
                dealer_dict['email{}'.format(e)] = tag.text.strip()
                e+=1
            else:
                dealer_dict['phone{}'.format(p)] = tag.text.strip()
                p+=1

        csv_writer.writerow([name, address, contact_person, dealer_dict.get('phone1'), dealer_dict.get('phone2'), dealer_dict.get('phone3'), dealer_dict.get('phone4'), dealer_dict.get('email1'), dealer_dict.get('email2')])

csv_file.close()
print("Done")