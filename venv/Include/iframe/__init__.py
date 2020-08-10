from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
bro=webdriver.Chrome('./chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是在iframe中必须切换
bro.switch_to.frame('iframeResult')
div=bro.find_element_by_id('draggable')

#动作链
action=ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)
for i in range(1,5):
    #perform（）立即执行动作链
    action.move_by_offset(17,0).perform()
    sleep(0.3)
action.release()
sleep(5)
bro.quit()

