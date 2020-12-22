from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
#네이버 캡챠를 우회하기 위한 방법
def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


id = 'ID' #네이버 아이디
pw = 'PW' #네이버 비밀번호

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('lang=ko_KR')
#아래 주석을 해제하게 되면 크롬창이 뜨지 않음.
#.add_argument('headless')  
#chrome_options.add_argument('--disable-gpu')




driver = webdriver.Chrome('C:/Users/21827960/Documents/chromedriver.exe', chrome_options=chrome_options) #webdriver 위치 입력 바람

driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.get('https://daum.net')


#1교시
driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/dangsamo/articles/961094?useCafeId=false') #pc버전 카페주소에다 앞에 m. 을 붙이면 자동으로 모바일 주소로 바뀜 !IFrame때문에 귀찮!
time.sleep(3)
driver.find_element_by_xpath('//*[@id="cbox"]').send_keys('출석') #'출석' 키입력
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/button').click()  #댓글달기 클릭
time.sleep(3600)
