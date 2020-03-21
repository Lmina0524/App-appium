# 1、需要用到appium客户端，所有需要导入appium
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
#模拟home键
driver.keyevent(3)
#模拟返回键
driver.keyevent(4)
#模拟回车键
driver.keyevent(66)