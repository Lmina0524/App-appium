import time
from appium import webdriver
from selenium.webdriver.common.by import By
# 定义一个字典，用来存放被测手机及app的相关数据
# 需要知道：手机系统，系统版本，手机的设备ID，app包名，app的启动名
from utils import get_element

des_cap = dict()

des_cap["platformName"] = 'android'
des_cap["PlatformVersion"] = '5.1.1'
des_cap["deviceName"] = 'emulator-5554'
des_cap["appPackage"] = 'com.android.settings'
des_cap["appActivity"] = '.Settings'

# 获取对应的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

wlan_btn = By.XPATH,"//*[@text='WLAN']"
get_element(driver,wlan_btn).click()

search_btn = By.ID,"com.android.settings:id/search"
get_element(driver,search_btn).click()

search_text = By.ID,"android:id/search_src_text"
get_element(driver,search_text).send_keys("123")

time.sleep(2)
get_element(driver,search_text).click()