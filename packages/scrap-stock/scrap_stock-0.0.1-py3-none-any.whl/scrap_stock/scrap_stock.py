#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
from IPython.display import display


# In[2]:


symbol = input("Enter the symbol:")
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')

driver.get(f'https://merolagani.com/CompanyDetail.aspx?symbol={symbol}#0')
driver.maximize_window()


# In[3]:


try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Price History']"))).click()
except:
    pass

result = []
max_pages = 50
page =1
while page <= max_pages:
    try:
        dates = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-striped table-hover']/tbody/tr/td[2]")))
        last_tp = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-striped table-hover']/tbody/tr/td[3]")))
        change = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-striped table-hover']/tbody/tr/td[4]")))
        high = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-striped table-hover']/tbody/tr/td[5]")))
        low = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-bordered table-striped table-hover']/tbody/tr/td[6]")))
   

        for i in range(max_pages):
            data ={'Dates': dates[i].text,'Last_tp':last_tp[i].text,'Change':change[i].text,'High':high[i].text,'Low':low[i].text}
    
            result.append(data)
    
        next_elements = driver.find_elements("xpath", "//a[@title ='Next Page']")
        if next_elements:
            next_elements[0].click()
        page +=1
    except:
        break


# In[5]:


df_data = pd.DataFrame(result)
display(df_data)


# In[6]:


df_data.to_excel('sanima_datafull_sele.xlsx', index=False)

