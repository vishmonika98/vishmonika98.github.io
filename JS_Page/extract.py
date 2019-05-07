from selenium import webdriver

import base64
import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get("http://localhost/Fractal/JS_Page/ifs.html")



#driver.find_element_by_id("a1").clear()
#driver.find_element_by_id("a1").send_keys("-0.5")

driver.find_element_by_id("sub_button").click()

time.sleep(25)

canv = driver.find_element_by_id("canvas")
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canv)

canvas_png = base64.b64decode(canvas_base64)

with open("ifs_images/canvas.png", 'wb') as f:
    f.write(canvas_png)