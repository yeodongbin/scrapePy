# pip install selenium
# pip install bs4
# 팬텀JS http://phantomjs.org/download.html
# pip install pymysql #데이터 베이스
# from selenium.webdriver.common.by import By
# 명시적 대기를 위해
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import sys

# 사전에 필요한 정보를 로드
main_url = 'http://www.saramin.co.kr/zf_user/'
search_url = 'http://www.saramin.co.kr/zf_user/talent/search'
id = "kitri"
password = "kitri0908"
file_name = "Saramin.txt"
ELEMENT_COUNT_PER_PAGE = 20
PAGE_COUNT = 10
start_age = 26
end_age = 28

# 드라이버 로드 # 윈도우용
driver = wd.Chrome(executable_path='chromedriver.exe')

# 사이트 접속, 로그인
driver.get(main_url)
driver.implicitly_wait(2)
driver.find_element_by_id('btn_tab_com').click()
driver.find_element_by_name('id').send_keys(id)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('login_btn').click()
driver.implicitly_wait(2)

driver.get(search_url)
driver.find_element_by_class_name('btn_box_close').click() #팝업없애기
driver.find_element_by_id('btn-display-save-list').click() #저장된 설정 가져오기
driver.implicitly_wait(2)

save_option_area = driver.find_element_by_id('save_option_area')
link_element = save_option_area.find_element_by_class_name('title')
link_element.click()
driver.implicitly_wait(2)

# 나이 입력
driver.find_element_by_xpath('//*[@id="max-age"]/option[10]').click()#26세
driver.find_element_by_xpath('//*[@id="min-age"]/option[4]').click() #28세
time.sleep(2) #페이지 이동간 대기

#Element 확인 (검색된 전체 인원 파악)
element_count = int(driver.find_element_by_id('resumeCnt').text.replace(',',''))
page_count = element_count // ELEMENT_COUNT_PER_PAGE # TOTAL PAGE COUNT
list_count = element_count // (ELEMENT_COUNT_PER_PAGE*PAGE_COUNT)

print('-------------------------------------------------------')
print(element_count, type(element_count))
print(page_count)
print(list_count)
print('-------------------------------------------------------')

f = open(file_name,'w')
count = 0;

# 페이지 이동하는 코드
count = 1
for next_count in range(1,2): #next 버튼
    pages_url = driver.find_elements_by_class_name("page")
    print(len(pages_url))

    for page_url in pages_url:
        print(len(pages_url))
        page_url.click()
        time.sleep(2)  # 페이지 이동간 대기

        #각 타이틀별로 url 이동
        current_url = driver.current_url #현재 url 저장
        people_title = []
        people_url = []
        people_title = driver.find_elements_by_xpath("//a[@class = 'title resumeSubject']")

        driver.get(current_url) #검색된 페이지로 이동
        driver.find_element_by_class_name('btn_box_close').click()  # 팝업없애기

    print("%s장 ok" % count)
    next_button = driver.find_elements_by_class_name('btn_next')
    next_button[1].click()
    time.sleep(3)
#__________________________________________________________________
f.close()
driver.close()
driver.quit()
sys.exit()


