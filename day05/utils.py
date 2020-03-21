from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_element(driver,element):
    try:
        wait = WebDriverWait(driver,5,1)
        ele = wait.until(lambda x:x.find_element(*element))
        return ele
    except:
        return None


def execute_tab(driver,element):
    if isinstance(element, tuple):
        element = get_element(driver,element)
    element.click()

def execute_input(driver,element,text):
    if isinstance(element,tuple):
        element = get_element(driver,element)
    element.clear()
    element.send_keys(text)