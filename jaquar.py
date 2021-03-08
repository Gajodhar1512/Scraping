import requests
import csv

dealers = requests.get('http://bindalcoir.com/dealers-locator/#1483094093667-299f9a26-82c5')

# csv_file = open('jaquar_dealers.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Name', 'Address1', 'Address2', 'State', 'City', 'Phone', 'Email'])

for dealer in dealers:
    print(dealer)
    print()
    name = dealer['Company']
    address1 = dealer.get('Address1')
    address2 = dealer.get('Address2')
    state = dealer.get('StateProvince')
    city = dealer.get('City')
    phone = dealer.get('PhoneNumber')        
    email = dealer.get('Email')

    # csv_writer.writerow([name, address1, address2, state, city, phone, email])

# csv_file.close()
print("Done")