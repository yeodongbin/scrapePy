
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import sys

# 사전에 필요한 정보를 로드
main_url = 'http://www.jobkorea.co.kr/Corp/Main'
search_url = 'http://www.jobkorea.co.kr/Corp/Person/FindByKey?key=bkFZGbH5eiM5qhQXmKw0GBV_QPacryptoMS7TmyjYuX8sjMoNkQS2fNRiIWQeBXFe5Fpf'
#platform_develop_url = 'http://www.gamejob.co.kr/List_GG/GG_Part_Search.asp?Part_Code=12&car_u=0&car_d=1&age_u=1999&age_d=1988&S_Keyword='
id = "kitriis"
password = "kitriis0908"
file_name = "JobKorea.txt"
total_num = 0

# 드라이버 로드 # 윈도우용
driver = wd.Chrome(executable_path='chromedriver.exe')

# 사이트 접속 (get)
driver.get(main_url)
driver.implicitly_wait(2)
driver.find_element_by_name('M_ID').send_keys(id)
driver.find_element_by_name('M_PWD').send_keys(password)
driver.find_element_by_class_name('btnLogin').click()
driver.implicitly_wait(2)
driver.get(search_url)
driver.implicitly_wait(2)


for page in range(2, 9):
    try :

        driver.execute_script("Javascript:data-page(this.form,%s)" % page)
    except Exception as e:
        print('오류 e ', e)