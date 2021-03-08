from selenium import webdriver
import time, csv

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.centuryply.com/NAP/Starke/store-locator')
time.sleep(3)

csv_file = open('centuryply_dealers.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dealer', 'Contact Person', 'Address', 'Phone', 'Email'])

for i in range(1,28):
    print()
    try:
        print(driver.find_element_by_xpath("//option[@value={}]".format(i)).text)
        driver.find_element_by_xpath("//option[@value={}]".format(i)).click()
    except:
        continue
    time.sleep(3)
    cities = driver.find_element_by_id('dealer_city').find_elements_by_tag_name('option')[1:]
    if len(cities) == 0:
        continue
    for city in cities:
        print(" " + city.text)
        city.click()
        time.sleep(2)
        pincodes = driver.find_element_by_id('store_pincode').find_elements_by_tag_name('option')[1:]
        if len(pincodes) == 0:
            continue
        for pin in pincodes:
            try:
                print("  " + pin.text)
                pin.click()
                time.sleep(2)
                dealer_div = driver.find_element_by_id('dealer_address_data')
                address = dealer_div.find_elements_by_tag_name('p')[0].text
                print("   " + address)
                contact_person = dealer_div.find_elements_by_tag_name('p')[1].text
                print("   " + contact_person)
                try:
                    name = dealer_div.find_elements_by_tag_name('p')[2].text
                    print("   " + name)
                except:
                    name=""
                try:
                    phone = dealer_div.find_elements_by_tag_name('p')[3].text
                    print("   " + phone)
                except:
                    phone=""
                try:
                    email = dealer_div.find_element_by_tag_name('a').text
                    print("   " + email)
                except:
                    email=""
            except:
                csv_writer.writerow(["", "", "", "", ""])
            csv_writer.writerow([name, contact_person, address, phone, email])

csv_file.close()
driver.quit()
print("------------DONE------------")