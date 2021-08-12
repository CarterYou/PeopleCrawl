import random
import time

import pyperclip as pyperclip
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup as bs
import beepy

options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')  # user-agent 이름 설정
request_headers = {'User-Agent':('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'),}

#Copy and Paste login information
driver = webdriver.Chrome('../source/chromedriver', options=options)

su_main = 'http://su.kau.ac.kr/sugang/main.su'
su_list = 'http://su.kau.ac.kr/sugang/favorites.su?mode=list'
su_cancel = 'http://su.kau.ac.kr/sugang/mypage.su?mode=saveList'

xpath_id = '//*[@id="j_username"]'
xpath_pass = '//*[@id="j_password"]'
xpath_connect = '/html/body/div[5]/div[2]/div[2]/div[1]/div/p/img'
xpath_ok_302 = '/html/body/div[4]/div[11]/div/button'

def req(html):
    xml = requests.get(html, headers=request_headers)
    return xml

if __name__ == "__main__":
    while True:
        driver.get(su_list)
        driver.implicitly_wait(10)
        #오류페이지
        if driver.current_url[0:35] == 'http://su.kau.ac.kr/sugang/error.su':
            print('login page access')
            #오류페이지 확인, 로그인페이지로 넘어가기
            driver.find_element_by_xpath(xpath_ok_302).click()
            driver.implicitly_wait(2)
            #아이디 비밀번호 입력
            driver.find_element_by_id('j_username').send_keys('2018124126')
            driver.find_element_by_id('j_password').send_keys('dbdldnjs1303@')
            #로그인
            driver.find_element_by_xpath(xpath_connect).click()
            #로그인 확인
            driver.implicitly_wait(10)
            if driver.current_url == su_main:
                print('login success')
                driver.get(su_list)
            else:
                print('login failed')
                print(driver.current_url)
        #접속 성공
        elif driver.current_url == su_list:
            print('list access success')
            cl = []
            table = driver.find_element_by_xpath('//*[@id="content"]/form/div/div/div/div/table/tbody')
            rows = table.find_elements_by_tag_name('tr')
            for index, value in enumerate(rows):
                cl_seat = value.find_elements_by_tag_name('td')[0].text
                cl_id = value.find_elements_by_tag_name('td')[1].text
                cl_name = value.find_elements_by_tag_name('td')[2].text
                cl_prof = value.find_elements_by_tag_name('td')[8].text
                cl_all_time = value.find_elements_by_tag_name('td')[10].text
                cl_my_time = value.find_elements_by_tag_name('td')[11].text
                cl_when = value.find_elements_by_tag_name('td')[12].text
                cl.append([cl_seat, cl_id, cl_name, cl_prof, cl_all_time, cl_my_time, cl_when])

            table = driver.find_element_by_xpath('//*[@id="content"]/form/div/div/div/div/table/tfoot')
            rows = table.find_elements_by_tag_name('tr')
            for index, value in enumerate(rows):
                cl_seat = value.find_elements_by_tag_name('td')[0].text
                cl_id = value.find_elements_by_tag_name('td')[1].text
                cl_name = value.find_elements_by_tag_name('td')[2].text
                cl_prof = value.find_elements_by_tag_name('td')[8].text
                cl_all_time = value.find_elements_by_tag_name('td')[10].text
                cl_my_time = value.find_elements_by_tag_name('td')[11].text
                cl_when = value.find_elements_by_tag_name('td')[12].text
                cl.append([cl_seat, cl_id, cl_name, cl_prof, cl_all_time, cl_my_time, cl_when])

            for i in cl:
                if i[2] == '디지털시스템설계' and i[0]=='신청':
                    print(i)
                    beepy.beep(sound="ping")
                elif i[2] == '글로벌문화와 소통' and i[0]=='신청':
                    print(i)
                    beepy.beep(sound="ping")
                else:
                    continue

            time.sleep(random.randrange(3,10))
        #에러
        else:
            print('unexpected error')
            break

        # try:
        #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[2]')))
        # except selenium.common.exceptions.TimeoutException:
        #     print('timeout')
        # else:
        #     print('found')
        # finally:
        #     driver.close()

"""
if 302
    확인 클릭 /html/body/div[4]/div[11]/div/button
    id : //*[@id="j_username"]
    pass : //*[@id="j_password"]
    ok : /html/body/div[5]/div[2]/div[2]/div[1]/div/p/img
    
    신청 /html/body/div[5]/div/form/div/div/div/div/table/tbody/tr[1]/td[1]/p/a
    여석없음 /html/body/div[5]/div/form/div/div/div/div/table/tbody/tr[2]/td[1]/p/a

else if 200
    find '신청' 
    if found
        카카오톡 알림

        if find 한게 기디실 도규봉, 이성욱
            connect to http://su.kau.ac.kr/sugang/mypage.su?mode=saveList
            기디실 취소
            back to http://su.kau.ac.kr/sugang/favorites.su?mode=list
            find 한 기디실 신청
            quit
            
        else if find 한게 디시설 정윤호, 김태환
            connect to http://su.kau.ac.kr/sugang/mypage.su?mode=saveList
            디시설 취소
            back to http://su.kau.ac.kr/sugang/favorites.su?mode=list
            find 한 기디실 신청
            quit
        else 
            카톡알림
            pass
    else 처음으로
else 처음으로
"""