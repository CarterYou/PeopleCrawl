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

#Copy and Paste login information
driver = webdriver.Chrome('../source/chromedriver')
site_list = {'https://cafe.naver.com/suhui?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10197921%26search.boardtype=L%26search.menuid=3847%26search.marketBoardTab=D%26search.specialmenutype=%26userDisplay=50'
}
xpath_id = '//*[@id="main-area"]/div[4]/table/tbody/tr[2]'

def copy_login(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
    time.sleep(2)

def xpathId():
    id = driver.find_element_by_xpath(xpath_id)
    print(id)

if __name__ == "__main__":
    for i in site_list:
        driver.get(i)
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[2]')))
        except selenium.common.exceptions.TimeoutException:
            print('timeout')
        else:
            print('found')
        finally:
            driver.close()
"""
수만휘 최종결과 기록
//*[@id="main-area"]/div[4]/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/a
//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/a
결과 : <a href="#" class="m-tcol-c" onclick="ui(event, 'rnqja15',3,'구국구','10197921','me', 'false', 'true', 'suhui', 'false', '3847'); return false;">구국구</a>
/html/body/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/a
"""
