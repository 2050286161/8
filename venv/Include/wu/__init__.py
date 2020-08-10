from selenium import webdriver
from time import sleep

from selenium.webdriver import  ChromeOptions
from selenium.webdriver.chrome.options import Options
#无可视化界面固定化搭配
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#实现规避检查固定搭配
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
#实现可视化，实现规避操作
bro=webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)
#无可视化界面
bro.get('https://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()