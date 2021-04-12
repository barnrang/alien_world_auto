from selenium import webdriver
import chromedriver_binary
import time

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

# driver.get('https://www.google.com/')
# print(driver.title)

# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# print(driver.title)

# driver.save_screenshot('search_results.png')
# driver.quit()

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://play.alienworlds.io/');
time.sleep(1000) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()