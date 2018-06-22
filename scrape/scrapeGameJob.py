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
import sys

# 사전에 필요한 정보를 로드
main_url = 'http://www.gamejob.co.kr/Login/Login_GI.asp'
search_url = 'http://www.gamejob.co.kr/List_GG/GG_Part_Search.asp?Part_Code=2&car_u=0&car_d=1&age_u=1999&age_d=1988&S_Keyword='
id = "kitri"
password = "kitri0908"
file_name = "GameJob.txt"

# 드라이버 로드 # 윈도우용
driver = wd.Chrome(executable_path='chromedriver.exe')

# 사이트 접속 (get)
driver.get(main_url)
driver.implicitly_wait(2)
driver.find_element_by_name('M_ID').send_keys(id)
driver.find_element_by_name('M_PWD').send_keys(password)
driver.find_element_by_id('send_img').click()
driver.implicitly_wait(2)

#파일 오픈
f = open(file_name,'w')
count = 0
for page in range(10, 12):
    try:
        driver.get(search_url)
        driver.execute_script("Javascript:go_db_page(this.form,%s)" % page)
        driver.implicitly_wait(2)
        print("\n********** %s 페이지 이동 **********\n" % page)
        people_url = []

        people_title = driver.find_elements_by_xpath("//td[@class = 'p_list']")
        #print(len(people_title), type(people_title))

        if (len(people_title))==22:
            del people_title[0:2]
            print(len(people_title), type(people_title))

        #개인 url 추출
        for p_title in people_title:
            try:
                p_url = p_title.find_element_by_css_selector('a').get_attribute('href')
                people_url.append(p_url)
            except Exception as e1:
                print('오류',e1)

        #url에 접속해 필요 정보 추출(Email, 이름)
        for p_url in people_url:
            try:
                count += 1
                print(count, p_url)

                try:
                    driver.get(p_url)
                    driver.implicitly_wait(2)
                    soup = bs(driver.page_source, 'html.parser')
                except Exception as e3:# 접속 불가시에 예외처리
                    alrt = driver.switch_to_alert()#popup close
                    alrt.accept()
                    print('오류 e3 ', e3)
                    continue

                #name , email 추출
                name_list = soup.findAll("font",{"class":"b c_skyblue"})
                name = name_list[0].get_text()
                print('Name : ', name)

                email_list = soup.findAll("font", {"class": "c_blue"})
                if len(email_list)>=1:# email 없을 경우 예외처리
                    email = email_list[0].get_text()
                    print('E-Mail : ',email)
                else:
                    email = "E-Mail 없음"
                    print("E-Mail 없음")

                #파일 입력
                f.write(str(count)+",")
                f.write(name[0:3]+",")
                f.write(email+"\n")
            except Exception as e2:
                print('오류 e2 ', e2)
                break
    except Exception as e:
        print('오류 e ', e)

# 종료
f.close()
driver.close()
driver.quit()
sys.exit()