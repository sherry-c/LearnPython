
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver-win64', 'chromedriver.exe')

wd = webdriver.Chrome(service=Service(driver_path))


# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序') 