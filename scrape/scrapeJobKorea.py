
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import sys

#함수 정의
def getLinks(source):
    websiteLinks = []
    for link in source.find_all('a'):
        url = link.get('href')
        if url:
            websiteLinks.append(url)

    for link in websiteLinks:
        print(link)

    return websiteLinks

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


# 페이지 이동
# pages = ['2','3']
# for page in pages:
#     print(type(page))
#     driver.find_element_by_partial_link_text(page).click()
#     driver.implicitly_wait(2)
# <a href="#" data-page="2">2</a>
# <a href="#" data-page="2">2</a>
# <a href="#" data-page="3">3</a>
#dvBasicResumeList > section > div.tplPagination.js-ListPaging > ul > li:nth-child(3) > a
#//*[@id="dvBasicResumeList"]/section/div[2]/ul/li[2]/a


#개인 정보 취합

#
# p_url = driver.find_element_by_id('linkResume2')
# url = p_url.find_element_by_css_selector('a').get_attribute('href')
# #people_id = driver.find_elements_by_id('linkResume2').get_attribute('href')
# print(url)
#print(people_id)
i = 0
# for p_url in people_url:
#     i += 1
#
#     # Keys.TAB
#     # Keys.TAB
#     # Keys.TAB
#     # Keys.ENTER
#     print(url)




# for page in range(2, 9):
#     try :
#         driver.execute_script("Javascript:data-page(this.form,%s)" % page)
#     except Exception as e:
#         print('오류 e ', e)

#driver.quit()