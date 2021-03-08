from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.centuryply.com/NAP/Starke/store-locator')

states = driver.find_elements_by_class_name('form-control input inp-chng drop-menu')
import pdb; pdb.set_trace()
# for option in el.find_elements_by_tag_name('option')[2:]:
#     print(option.text)
#     option.click()
#     time.sleep(3)
#     search = driver.find_element_by_id('storeLocatorSearch')
#     time.sleep(1)
#     search.click()
#     dealers = driver.find_elements_by_class_name('store_detail')
#     for dealer in dealers[::-1]:
#         print(dealer.text)
#         dealers.remove(dealer)
    
#     time.sleep(3)


driver.quit()