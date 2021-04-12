from PIL import Image
import io
import numpy as np

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import matplotlib.pyplot as plt

canvas = driver.find_element_by_id('unityContainer')
style_element = [x.strip() for x in canvas.get_attribute('style').split(';')]
width = int(style_element[0].split(' ')[-1][:-2])
height = int(style_element[1].split(' ')[-1][:-2])

mining_button_ref = plt.imread('alien_images/mining_button.png')
claim_button_ref = plt.imread('alien_images/claim_button.png')
return_to_mine_ref = plt.imread('alien_images/return_to_mine.png')

def press_mining(posx=0, posy=0):
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(canvas, posx, posy)
    action.click()
    action.perform()

def check_if_can_mine():
    data = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(data))
    mining_button = np.asarray(img)[740:760, 600:650].astype(np.float32) / 255.
    return (np.mean(np.abs(mining_button_ref - mining_button)) < 0.01)

def check_if_can_claim():
    data = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(data))
    mining_button = np.asarray(img)[400:450, 400:450].astype(np.float32) / 255.
    return (np.mean(np.abs(claim_button_ref - mining_button)) < 0.01)

def check_if_can_return():
    data = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(data))
    mining_button = np.asarray(img)[680:700, 250:300].astype(np.float32) / 255.
    return (np.mean(np.abs(return_to_mine_ref - mining_button)) < 0.01)

mining_pos = (510, 600)
claim_pos = (510, 400)
return_to_mining_pos = (200, 560)

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://play.alienworlds.io/')
print('Please login and enter the page before press mining')
print('Enter "y" and press enter if ready: ')
while input() != 'y':
    print('Please enter "y" and press enter if ready whenever you are ready:)))): ')

while True:
    print('Prepare to mine')
    while not check_if_can_mine():
        time.sleep(20)
    press_mining(*mining_pos)
    
    print('Prepare to claim')
    while not check_if_can_claim():
        time.sleep(20)
    press_mining(*claim_pos)
    
    print('Prepare to return')
    while not check_if_can_return():
        time.sleep(20)
    press_mining(*return_to_mining)


driver.quit()