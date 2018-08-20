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
search_count = 100 # 찾는 자료 갯수 설저
start_age = 0    # 검색 시작 나이<동작안함
end_age = 0      # 검색 시작 나이<동작안함

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
#driver.find_element_by_id('max-age').find_element_by_link_text("26세 (1993년)").click()
#driver.find_element_by_id('min-age').find_element_by_link_text("28세 (1991년)").click()
#driver.find_element_by_xpath('//*[@id="max-age"]/option[13]').click()#29
#driver.find_element_by_xpath('//*[@id="min-age"]/option[4]').click() #31
driver.find_element_by_xpath('//*[@id="max-age"]/option[10]').click() #26
driver.find_element_by_xpath('//*[@id="min-age"]/option[4]').click()  #28
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
for next_count in range(1,page_count): #next 버튼
    pages_url = driver.find_elements_by_class_name("page")
    #driver.find_element_by_xpath('//*[@id="pagingArea"]/div/button[10]').click()
    for index in range(0,11):
        pages_url = driver.find_elements_by_class_name("page")
        pages_url[index].click()
        time.sleep(2)  # 페이지 이동간 대기

        #각 타이틀별로 url 이동
        current_url = driver.current_url #현재 url 저장
        people_title = []
        people_url = []
        people_title = driver.find_elements_by_xpath("//a[@class = 'title resumeSubject']")

        #각 타이틀의 URL 저장 (20개씩)
        for p_title in people_title:
            try:
                p_url = p_title.get_attribute('href')
                people_url.append(p_url)
            except Exception as e2:
                print('오류', e2)

        #각 타이틀의 URL로 이동
        for p_url in people_url:
            try:
                driver.get(p_url) #
                obscured_element = None
                time.sleep(2)  # 페이지 이동간 대기

                #가려진 항목 선택
                try:
                    obscured_element = driver.find_element_by_xpath('// *[ @ id = "resume_print_area"] / div / div[1] / div[2] / div[2] / ul / li[1] / a')
                except Exception as e:
                    pass

                if (obscured_element):
                    obscured_element.click()
                    time.sleep(2)

                p_info = driver.find_element_by_class_name('myname').text
                phone = driver.find_element_by_class_name('phone').text
                email = driver.find_element_by_class_name('mail').text
                print(count,p_info[:3],phone[:14],email)

                # 파일 입력
                if email!='비공개':
                    f.write(str(count) + ",")
                    f.write(p_info[:3] + ",")
                    f.write(phone[:14] + ",")
                    f.write(email + "\n")
                    if count ==search_count:
                        print("searching complete!!")
                        sys.exit(1)

                    count += 1
            except Exception as e1:
                print('오류')
                continue
        driver.get(current_url) #검색된 페이지로 이동
        driver.find_element_by_class_name('btn_box_close').click()  # 팝업없애기

    print("%s장 ok" % count)
    next_button = driver.find_elements_by_class_name('btn_next')
    next_button[0].click()
    time.sleep(3)
#__________________________________________________________________
f.close()
driver.close()
driver.quit()
sys.exit()


