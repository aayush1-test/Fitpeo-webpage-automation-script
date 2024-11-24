
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys

import pyautogui  #(used 'pyautogui' package to perform key action)

driver=webdriver.Chrome()
driver.get("https://fitpeo.com/")  #(Fitpeo webpage url)
driver.maximize_window()

#(Nagaigate to Revenue calculator)
driver.find_element(By.XPATH,"(//div['satoshi MuiBox-root css-r3xbt7'])[17]").click()
import time
time.sleep(3)

#(To scroll the page down to the slider bar)
element = driver.find_element(By.XPATH, "(//p['MuiTypography-root MuiTypography-body1 inter css-k0m0w'])[8]")
driver.execute_script("arguments[0].scrollIntoView();", element)
import time
time.sleep(3)

#(To change the position of sliderbar)
act=ActionChains(driver)
sliderbar=driver.find_element(By.XPATH,"//span[@class='MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh']")
act.perform()

act.drag_and_drop_by_offset(sliderbar,94,0).perform()
act.click_and_hold(on_element=sliderbar)
time.sleep(3)
#Since offset doesn't provides exact value for 820,so used 'pyautogui' package to perform left arrow key button.

pyautogui.press('left')
pyautogui.press('left')
act.release(on_element=sliderbar)

#(Navaigate to slider input box)
driver.find_element(By.XPATH,"//input[@type='number']").click()
time.sleep(3)
pyautogui.press('backspace')  #(used 'pyautogui' package to perform key action)
pyautogui.press('backspace')
pyautogui.press('backspace')


driver.find_element(By.XPATH,"//input[@type='number']").send_keys("560")
time.sleep(3)
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='number']").send_keys("820")
time.sleep(2)

#(Navigate to CPT code box)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]").click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]").click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[8]").click()

time.sleep(5)