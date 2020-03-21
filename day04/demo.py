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
# 获取当前的包名
print(driver.current_package)
# 获取当前app的启动名
print(driver.current_activity)
# 获取当前app的上下文  NATIVE_APP代表的是原生的app，是指开发过程当中全部代码是通过android开发人员通过java代码和android-sdk开发出来的app
print(driver.current_context)

# 关闭当前app
driver.close_app()

# 启动app
driver.start_activity("com.baidu.homework",".activity.init.InitActivity")

# 将作业帮置后台运行3秒钟
driver.background_app(3)