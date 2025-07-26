from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

chrome_driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver-win64', 'chromedriver.exe')


def initial_browser():
    q1 = Options()
    # 禁用浏览器沙盒模式
    q1.add_argument('--no-sandbox')
    # 保持浏览器是打开状态
    q1.add_experimental_option('detach', True)

    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    wd = webdriver.Chrome(
        service=Service(chrome_driver_path),
        options=q1)
    wd.implicitly_wait(10)
    return wd


wd = initial_browser()
# 打开指定网址
# wd.get('https://www.baidu.com/')
# https://bahuyun.com/bdp/form/1327923698319491072
# https://sahitest.com/demo/alertTest.htm
# wd.get('https://sahitest.com/demo/promptTest.htm')

# P27 网页前进 后退
wd.get('https://www.baidu.com/')
wd.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[6]/div/div/form/span[1]/input')[0].send_keys('apple')
time.sleep(1)
wd.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[6]/div/div/form/span[2]/input')[0].click()
time.sleep(1)
wd.back()
time.sleep(1)
wd.forward()

#aaa

# P26 获取元素文本内容 是否可见
# wd.get('https://news.cri.cn/20250723/950b47a9-e4fd-db7c-874f-1fc3e88cde37.html')
# # 获取元素文本内容text
# text = wd.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/p[1]')[0].text
# print(text)
#
# # 元素是否可见
# res = wd.find_elements(By.XPATH, '/html/body/script[6]')[0].is_displayed()
# print(res)

# P25 iframe 嵌套页面进入 退出
# wd.get('https://sahitest.com/demo/iframesTest.htm')
# # 获取iframe元素
# iframe = wd.find_elements(By.XPATH, '/html/body/iframe')
#
# # 切换到嵌套的页面
# wd.switch_to.frame(iframe[0])
# wd.find_elements(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]')[0].click()
# # 退出嵌套的页面
# wd.switch_to.default_content()
# wd.find_elements(By.XPATH, '/html/body/input[2]')[0].click()

# P24 提示框 prompt 元素交互
# wd.find_elements(By.XPATH, '/html/body/form/input[1]')[0].click()
# time.sleep(1)
# wd.switch_to.alert.send_keys('123abc')
# time.sleep(2)
# wd.switch_to.alert.accept()



# # P23 确认框 confirm 元素交互
# wd.find_elements(By.XPATH, '/html/body/form/input[1]')[0].click()
# time.sleep(1)
# # wd.switch_to.alert.accept()
# wd.switch_to.alert.dismiss()


# # P22 警告框 alert 元素交互
# wd.find_elements(By.XPATH, '/html/body/form/input[2]')[0].click()
# time.sleep(1)
# # 点击弹窗确定按钮
# # wd.switch_to.alert.accept()
#
# # 获取弹窗的文本
# print(wd.switch_to.alert.text)

# # P21 获取句柄 切换标签页
# wd.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[3]')[0].click()
#
# # 获取全部标签页句柄,返回值是一个列表
# pages = wd.window_handles
# print(pages)
#
# # 关闭之前的标签页
# wd.close()
# # 通过句柄切换标签页
# wd.switch_to.window(pages[1])
#
# # 获取当前标签页的句柄
# page = wd.current_window_handle
# print(f'the current handle is :{page}')

# P20 日期 评星 上传文件
# 填写日期 send_keys
# 评星 click
# 上传文件 send_keys 要用绝对路径

# P19 元素交互 单选框 多选框 下拉元素交互
# 单选框 多选框 下拉元素直接点击
# click

# P18 元素定位隐性等待
# 元素定位等待(多少秒内找到元素就立刻执行 没有找到元素就报错)
# wd.implicitly_wait(10)
# wd.find_elements(By.XPATH, '/html/body/div[1]/div[6]/div[1]/div[1]/div/ul/li[3]/a[2]')[0].click()


# 浏览器的通用设置
# selenium库的8种定位方式

# P17 元素定位 XPATH  常用
# 1.复制谷歌浏览器 xpath 通过属性+路径定位
# 2.复制完整的XPATH 优点是基本上100%能定位到元素 缺点是定位值比较长
# wd.find_elements(By.XPATH, '//*[@id="s-top-left"]/a[1]')[0].click()
# wd.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]')[0].click()


# P16 元素定位-CSS_SELECTOR
# 1. #id = 井号#+id值 通过id定位
# 2. .class = 点+class通过class来定位
# 3. 不加修饰符 = 标签头 TAG_NAME
# 4. 通过任意类型来定位 "[类型='精准值']"
# 5. 通过任意类型来定位 "[类型*='模糊值']"
# 6. 通过任意类型来定位 "[类型^='开头值']"
# 7. 通过任意类型来定位 "[类型$='结尾值']"
# 以上是理论定位方式
# 8. 更简单的定位方式 在chrome里面直接复制SELECTOR
#    系统会自动给出唯一的定位值,缺点是个别元素的定位值可能会比较长


# wd.find_element(By.CSS_SELECTOR, '#kw').send_keys('apple')
# wd.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, 'input')[7].send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, "[autocomplete='off']")[0].send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, "[autocomplete*='of']")[0].send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, "[autocomplete^='o']")[0].send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, "[autocomplete$='f']")[0].send_keys('apple')
# wd.find_elements(By.CSS_SELECTOR, "#s-top-left > a:nth-child(3)")[0].click()



# P15 元素定位-PARTIAL_LINK_TEXT
# 通过模糊连接文本找到标签a的元素[模糊文本定位]
# 有重复的文本需要切片
# wd.find_element(By.PARTIAL_LINK_TEXT, '地').click()


# P14 元素定位-LINK_TEXT
# 通过a标签的内容找到对应的元素
# 通过精准连接文本找到标签a元素
# wd.find_element(By.LINK_TEXT, '地图').click()


# P13
# 元素定位 TAG_NAME
# 1.查找<开头标签名字>
# 2.重复的标签名字有很多，需要切片处理
# document.getElementsByClassName('s_ipt')
# element1 = wd.find_elements(By.TAG_NAME, 'input')
# print(element1)
# element1[7].send_keys('stock')
# wd.find_elements(By.TAG_NAME, 'a')[3].click()


# P12
# 元素定位class name
# 在浏览器的console里面确认一下有没有重复的元素
# document.getElementsByClassName('s_ipt')
# element1 = wd.find_element(By.CLASS_NAME, 's_ipt')
# print(element1)
# element1.send_keys('stock')
# element2 = wd.find_element(By.ID, 'su')
# print(element2)
# element2.click()
# 1.class值不能有空格，否则报错
# 2.class重复的值很多时，切片操作
# 3.class值有的网站是随机的

# 打开bilibili电机番剧 https://www.bilibili.com/
# element1 = wd.find_elements(By.CLASS_NAME, 'channel-icons__item')
# print(element1)
# element1[0].click()

# P11
# 元素定位NAME
# element1 = wd.find_element(By.NAME, 'wd')
# print(element1)
# element1.send_keys('stock')
# 1.通过NAME定位元素 一般比较准确
# 2.并不是所有网页或者元素都有NAME值


# P10
# 元素定位的ID
# element1 = wd.find_element(By.ID, 'kw')
# 1.通过ID定位元素 一般比较准确
# 2.并不是所有网页或者元素都有ID值


# P9
# 元素交互操作
# 元素点击 click
# 元素输入 send_keys
# 元素清空 clear
# element1 = wd.find_element(By.ID, 'kw')
# print(element1)
# element1.send_keys('stock')
# time.sleep(2)
# # 元素清空
# element1.clear()
# time.sleep(2)
# # 元素输入
# element1.send_keys('stock')
# element2 = wd.find_element(By.ID, 'su')
# time.sleep(2)
# element2.click()


# P8
# 元素定位
# 定位一个元素
# 定位多个元素
# 浏览器查找多个元素
# 元素定位导包  from selenium.webdriver.common.by import By

# 定位一个元素 找到的话返回结婚，找不到就报错
# element1 = wd.find_element(By.ID, 'kw')
# print(element1)
# element1.send_keys('stock')
# time.sleep(2)
# # 元素清空
# element1.clear()
# time.sleep(2)
# # 元素输入
# element1.send_keys('stock')
# element2 = wd.find_element(By.ID, 'su')
# time.sleep(2)
# element2.click()

# # 定位多个元素 找到的话返回元素列表 找不到的话返回空列表
# element2 = wd.find_elements(By.ID, 'kw')
# print(element2)

# 浏览器查找多个元素 找一下浏览器的控制台
# document.getElementById('title')


# P7
# 浏览器截图 网页刷新
# wd.get_screenshot_as_file('1.png')
# time.sleep(1)
# wd.refresh()


# P6
# 浏览器打开位置和打开尺寸
# wd.set_window_position(200,0)
# wd.set_window_size(800,600)


# P5
# 浏览器最大化 最小化
# wd.maximize_window()
# time.sleep(3)
# wd.minimize_window()


# P4
# time.sleep(3)
# 关闭当前标签页
# wd.close()

# time.sleep(2)
# 关闭当前浏览器并释放驱动
# wd.quit()


# input('等待回车键结束程序')
# wd.implicitly_wait(10)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.byhy.net/cdn2/files/selenium/stock1.html')
#
# element = wd.find_element(By.ID, 'kw')
#
# element.send_keys('通讯\n')

# 返回页面 ID为1 的元素
# element = wd.find_element(By.ID, '2')
# 打印该元素的文字内容
# print(element.text)