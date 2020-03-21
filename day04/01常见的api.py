#1、需要用到appium客户端，所以需要导入appium
from appium import webdriver
#定义一个字典，用来存放被测手机及app的相关数据
#需要知道  手机系统、系统的版本、手机的设备ID、app包名、app的启动名
des_cap = dict()  #定义了一个空字典
#添加具体的参数值
des_cap["platformName"] = 'android'  # 设置当前平台的系统
des_cap["platformVersion"] = '5.1.1' # 设置平台的版本
des_cap["deviceName"] = 'emulator-5554' #设置手机的设备ID， 如果当前只有一个手机或模拟器可以用 *** 代替
des_cap["appPackage"] = 'com.android.settings'  # 设置app的包名
des_cap["appActivity"] = '.Settings'  # 设置app的启动名
# 获取对应的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", des_cap)

#获取当前app的包名
print(driver.current_package)
#获取当前app的启动名
print(driver.current_activity)
#获取当前app的上下文
# NATIVE_APP 代表的是原生的app  是指开发过程当中全部代码是通过android开发人员
# 通过java代码android-sdk开发出来的app（android开发和IOS）
#webapp  这个webapp全部是由前端开发人员通过HTML5开发出来的app，可以同时适合IOS和安卓
#混合app   是指在原生的app当中嵌入了H5的页面。（既有前端又有安卓和IOS开发）
#电商平台每周都会做活动，这些活动页面
print(driver.current_context)