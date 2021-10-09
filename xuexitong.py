from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头浏览器
bro = webdriver.Chrome(executable_path=r'谷歌驱动的绝对路径',options=chrome_options)  # 实例化对象
bro.get('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')  # 学习通登录url
username_tag = bro.find_element_by_id('phone')
username_tag.send_keys('your_mobile_phone')
password_tag = bro.find_element_by_id('pwd')
password_tag.send_keys('your_passwd')
btn = bro.find_element_by_id('loginBtn')
btn.click()
sleep(5)
bro.get('http://office.chaoxing.com/front/web/apps/forms/fore/apply?uid=131814638&code=vGh1maqe&mappId=5300924&appId=3c9c9642139643ba91477f442d69becc&appKey=l2E6J3d1g0B%2F5bCG&id=14788&enc=06fbc4bd4c56c44afabca4103d961275&state=121890&formAppId=&fidEnc=5901ab09a9ed3537')  # 健康填报url
sleep(5)
aniu = bro.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[2]/div[1]')
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
# sleep(5)
bro.quit()
