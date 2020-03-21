# 1、需要用到appium客户端，所有需要导入appium
import time
from appium import webdriver

# 定义一个字典，用来存放被测手机及app的相关数据
# 需要知道：手机系统，系统版本，手机的设备ID，app包名，app的启动名
des_cap = dict()

des_cap["platformName"] = 'android'
des_cap["PlatformVersion"] = '5.1.1'
des_cap["deviceName"] = 'emulator-5554'
des_cap["appPackage"] = 'com.android.settings'
des_cap["appActivity"] = '.Settings'

# 获取对应的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
#id
# driver.find_element_by_id("com.android.settings:id/title").click()
#class_name
# driver.find_element_by_class_name("android.widget.TextView").click()
#XPath
# driver.find_element_by_xpath("//*[@text = 'WLAN']").click()

driver.find_element_by_id("com.android.settings:id/search").click()

time.sleep(3)

driver.find_element_by_class_name("android.widget.ImageButton").click()
