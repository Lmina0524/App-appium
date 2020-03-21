#1、获取包名和启动名 包括手机设备ID
#'com.baidu.homework.activity.init.InitActivity'
#'com.baidu.homework'
#2、在查看元素工具中保存页面的元素信息(保存页面之前需要分析用到的页面)
#3、开始写代码


#1、需要用到appium客户端，所以需要导入appium
import time
from appium import webdriver
#定义一个字典，用来存放被测手机及app的相关数据
#需要知道  手机系统、系统的版本、手机的设备ID、app包名、app的启动名
from selenium.webdriver.common.by import By
from utils import get_element
des_cap = dict()  #定义了一个空字典
#添加具体的参数值
des_cap["platformName"] = 'android'  # 设置当前平台的系统
des_cap["platformVersion"] = '5.1.1' # 设置平台的版本
des_cap["deviceName"] = 'emulator-5554' #设置手机的设备ID， 如果当前只有一个手机或模拟器可以用 *** 代替
des_cap["appPackage"] = 'com.baidu.homework'  # 设置app的包名
des_cap["appActivity"] = 'com.baidu.homework.activity.init.InitActivity'  # 设置app的启动名
des_cap["resetKeyboard"] = True # 重置设备的输入键盘
des_cap["unicodeKeyboard"] = True # 采用unicode码输入
# 获取对应的连接
driver=webdriver.Remote("http://localhost:4723/wd/hub", des_cap)
#跳过按钮
skip_btn = By.XPATH, "//*[@text='跳过']"
#学生选择项
student_btn = By.ID, "com.baidu.homework:id/identity_student"
#年级选择
class_btn = By.XPATH, "//*[@text='一年级']"
#完成按钮
finish_btn = By.ID, "com.baidu.homework:id/information_entry_completion"
#弹层元素  需要点击两次  toast弹层
pop_window = By.CLASS_NAME, "android.view.View"
time.sleep(2)
#点击跳过按钮
get_element(driver, skip_btn).click()
#选择身份
get_element(driver, student_btn).click()
#选择年级
get_element(driver, class_btn).click()
#点击完成
get_element(driver, finish_btn).click()
#点击两次弹层的处理
for i in range(2):
    get_element(driver, pop_window).click()
    time.sleep(1)

