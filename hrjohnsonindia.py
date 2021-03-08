from selenium import webdriver
import time, csv

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.hrjohnsonindia.com/dealers')
time.sleep(2)

csv_file = open('hrjohnsonindia.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Dealer', 'Address', 'City', 'State', 'Phone', 'Deals_In'])

for i in range(0,37):
    driver.refresh()
    time.sleep(1)
    states = driver.find_element_by_name('state').find_elements_by_tag_name('option')
    print()
    state = states[i]
    print(state.text)
    state.click()
    time.sleep(1)
    cities = driver.find_element_by_name('city').find_elements_by_tag_name('option')[1:]
    if len(cities) == 0:
        continue
    for c in range(len(cities)-1):
        driver.refresh()
        time.sleep(1)
        states = driver.find_element_by_name('state').find_elements_by_tag_name('option')
        state = states[i]
        state_name = state.text
        state.click()
        time.sleep(1)
        cities = driver.find_element_by_name('city').find_elements_by_tag_name('option')[1:]
        print(len(cities))
        print(c)
        city = cities[c]
        city_name = city.text
        print(" "+city_name)
        city.click()
        time.sleep(1)
        dealers = driver.find_elements_by_class_name('desc-tle-lhs')
        if len(dealers) == 0:
            continue
        for dealer in dealers:
            name = dealer.find_element_by_class_name('prd-tle-name').text
            print("  "+name)
            add_deal = dealer.find_elements_by_class_name('prd-tle-brnd')
            address = add_deal[0].text
            print("  "+address)
            try:
                phone = add_deal[1].text
                print("  "+phone)
            except:
                phone = ""
            try:
                deals_in = add_deal[2].text
                print("  "+deals_in)
            except:
                deals_in = ""            

            csv_writer.writerow([name, address, city_name, state_name, phone, deals_in])

csv_file.close()
driver.quit()
print("------------DONE------------")