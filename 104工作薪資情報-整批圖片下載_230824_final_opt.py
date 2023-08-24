#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver_manager')


# In[5]:


#查看版本
import selenium
print(selenium.__version__)


# In[11]:


get_ipython().run_line_magic('time', '')

#匯入必要套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime

# 定義函數來打開網站並選擇職位
def open_website_and_select_job(title):
    # 設置 Chrome 選項
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 打開網站
    os.chdir("C:\\Users\\USER\\OneDrive\\0_Jupiter_save")
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get("https://guide.104.com.tw/salary/")

    # 點選搜尋bar，產生下拉式選單
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='輸入職務或選類別']").send_keys(title)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='輸入職務或選類別']").click()
    time.sleep(3)

    # 了解目前有哪些keyword職缺(下單式選單項目)
    elements = driver.find_elements(By.CLASS_NAME,'menuItem.cursor-pointer')
    n=0
    for element in elements:
        print('第'+str(n)+'行:',element.text)
        n+=1

    # 選擇想要的keyword職缺
    title_want = int(input("請輸入想要第幾個工作內容"))
    title_job = driver.find_elements(By.CLASS_NAME, 'menuItem.cursor-pointer')[title_want].text

    # 確定符合職稱，再次點選[確保[3].text皆一致]
    driver.find_elements(By.CLASS_NAME, 'menuItem.cursor-pointer')[title_want].click()

    # 點擊搜尋，產生url
    driver.find_element(By.CSS_SELECTOR, 'button').click()

    # 等待新的網址載入
    WebDriverWait(driver, 6).until(lambda d: "workexp" in d.current_url)

    # 產生目前網址
    url_now = driver.current_url
    url_now = url_now.replace("workexp", "{}")

    return driver, url_now, title_job

# 定義函數來擷取薪資資訊圖片
def capture_salary_images(driver, url_now, title_job):
    # 輸入欲查詢分頁
    search = ['mix', 'workexp', 'area', 'industry', 'edu', 'scale']
    driver.set_window_size(1200, 900)

    # 更改路徑
    os.chdir('C:\\Users\\USER\\OneDrive\\0_Jupiter_save\\104職業薪資水位_整批圖片下載')

    # 建立新檔並將檔案移至新資料夾
    if not os.path.isdir(title_job):
        os.mkdir(title_job)
        print('建立', title_job, '資料夾完成')
    os.chdir(f'./{title_job}')

    # 逐步開啟分頁印出
    for i in range(len(search)):
        driver.get(url_now.format(search[i]))
        driver.execute_script("document.body.style.zoom='0.5';") #縮小視窗
        time.sleep(5)

        # 網頁截圖
        date = str(datetime.date.today())
        pic_name = date + '_' + title_job + '_' + str(i) + '_' + search[i] + '.png'
        driver.save_screenshot(pic_name)
        print('完成截圖', pic_name)

    driver.quit()

# 主要程式執行
title = input("請輸入想要搜尋的職位")  # ex:區塊鏈
driver, url_now, title_job = open_website_and_select_job(title)
capture_salary_images(driver, url_now, title_job)


# In[ ]:


# 關閉 WebDriver
driver.quit()


# In[ ]:




