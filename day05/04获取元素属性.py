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
# 获取wlan的name值
print(get_element(driver, wlan_btn).get_attribute("name"))
#获取wlan的Class的值
print(get_element(driver, wlan_btn).get_attribute("className"))
# 获取resource-id的值
print(get_element(driver,wlan_btn).get_attribute("resourceId"))