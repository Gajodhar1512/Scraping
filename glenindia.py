from bs4 import BeautifulSoup
import requests
import csv


urls = [
    'https://www.glenindia.com/dealers/get/city/dealer/Bihar/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Uttarakhand/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Andhra%20Pradesh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Arunachal%20Pradesh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Goa/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Gujarat/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Haryana/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Jammu%20and%20Kashmir/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Jharkhand/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Karnataka/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Kerala/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Assam/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Maharashtra/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Odisha/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Punjab/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Rajasthan/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Tamil%20Nadu/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Telangana/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Uttar%20Pradesh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/West%20Bengal/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Chandigarh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Chhattisgarh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Delhi/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Himachal%20Pradesh/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Odisha/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Nagaland/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Mizoram/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Meghalaya/state',
    'https://www.glenindia.com/dealers/get/city/dealer/Madhya%20Pradesh/state'
]

csv_file = open('glenindia_dealers.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Address1','Address2','Location','City','State','Pin Code','mobile','phone','email', 'Contact Person'])

for url in urls:
    print(url)
    dealers = requests.get(url).json()
    active_dealers = [dealer for dealer in dealers['locations'] if dealer['deleted_at'] is None]   

    for dealer in active_dealers:
        print(dealer)
        print()
        name = dealer['name']
        address1 = dealer.get('address1').replace('<br>', " ")
        address2 = dealer.get('address2')
        location = dealer.get('location')
        city = dealer.get('city')
        state = dealer.get('state')
        pin = dealer.get('pincode')
        mobile = dealer.get('mobile')
        phone = dealer.get('phone')
        email = dealer.get('email')
        contact_person = dealer.get('contact_person')

        csv_writer.writerow([name,address1,address2,location,city,state,pin,mobile,phone,email,contact_person])

csv_file.close()
print("Done")
