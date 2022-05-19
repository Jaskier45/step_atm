import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )
    browser.find_element_by_css_selector("#book").click()
    
    data = browser.find_element_by_css_selector("#input_value")
    x = data.text
    inp = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(inp)
    browser.implicitly_wait(1)
    chose = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", chose)
    chose.click()
    
    # alr = browser.switch_to.alert
    # print(alr.text.split()[-1])
    # alr.accept()

except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    browser.quit()
