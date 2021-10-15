from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

#PS：本文不含有任何妨害防疫政策的暗示，亦不对使用本工具后产生的后果负责，如果您使用了本工具，默认已经接受了此规则
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头浏览器
bro = webdriver.Chrome(executable_path=r'F:/test/chromedriver.exe',options=chrome_options)  # 实例化对象
bro.get('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')  # 学习通登录url
username_tag = bro.find_element_by_id('phone')
username_tag.send_keys('phone')#手机号
password_tag = bro.find_element_by_id('pwd')
password_tag.send_keys('passwd')#密码
btn = bro.find_element_by_id('loginBtn')
btn.click()
sleep(5)
bro.get('https://uc.chaoxing.com/mobileSet/homePage?fid=121890&customizecolor=0xFFFFFF&time=20210103085130342&enc=EE9D0B4C0E4393B0C64851D542A6E14F')  # 健康填报url
sleep(5)
aniu = bro.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]')
aniu.click()
sleep(5)
morning_tag = bro.find_element_by_xpath('//*[@id="10"]/div[3]/input')
morning_tag.send_keys('36.6')
noon_tag = bro.find_element_by_xpath('//*[@id="11"]/div[3]/input')
noon_tag.send_keys('36.7')
night_tag = bro.find_element_by_xpath('//*[@id="12"]/div[3]/input')
night_tag.send_keys('36.5')
no_tag = bro.find_element_by_xpath('//*[@id="13"]/div[3]/input')
no_tag.send_keys('无')
b = bro.find_element_by_xpath('//*[@id="forms"]/div[2]/div[5]/div/div[2]/p')
b.click()
sleep(10)
bro.quit()
