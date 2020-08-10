from selenium import webdriver
from time import sleep

bro=webdriver.Chrome('./chromedriver.exe')

bro.get('https://qzone.qq.com')

bro.switch_to.frame('login_frame')

a_tag=bro.find_element_by_xpath('//*[@id="switcher_plogin"]')
a_tag.click()

userName_tag=bro.find_element_by_id('u')
userPassword_tag=bro.find_element_by_id('p')

userName_tag.send_keys('2050286161')
userPassword_tag.send_keys('x2932208983jl@')

a_tagl=bro.find_element_by_id('login_button')
a_tagl.click()
sleep(5)

bro.quit()
