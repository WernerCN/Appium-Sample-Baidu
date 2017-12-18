# -*- coding: utf-8 -*-：
from appium import webdriver
import time

# deviceName : adb device获得
# unicodeKeyboard,resetKeyboard : 使用Appium默认键盘
desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.1', 'deviceName': 'b8ad8dd1',
                'unicodeKeyboard': 'True', 'resetKeyboard': 'True', 'appPackage': 'com.baidu.searchbox',
                'appActivity': 'com.baidu.searchbox.SplashActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 设置等待超时
driver.implicitly_wait(5)
time.sleep(2)

# 闪屏界面点击立即体验
a = driver.find_element_by_id("introduction_entrance").click()
time.sleep(2)

# 进入搜索界面点击搜素框,跳转至搜索页面
driver.find_element_by_id("baidu_searchbox").click()

# 录入搜索内容
driver.find_element_by_id("SearchTextInput").send_keys(u"baidu")
time.sleep(2)

# 点击进行搜索
driver.find_element_by_id("float_search_or_cancel").click()
time.sleep(2)
driver.quit()
