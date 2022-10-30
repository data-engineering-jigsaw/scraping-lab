import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
headers={"User-Agent": "Googlebot"}


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
    driver = webdriver.Firefox(executable_path=r'/Users/jeffreykatz/Downloads/geckodriver')
    driver.get("http://www.indeed.com/jobs?q=data+engineer&l=New+York%2C+NY&vjk=67f4c335f087a0eb")
    driver.find_element(By.TAG_NAME, 'html')
    return driver.page_source

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  pass
  
  

  