import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
    driver = webdriver.Firefox(executable_path=r'/Users/jeffreykatz/Downloads/geckodriver')
    driver.get("http://www.indeed.com/jobs?q=data+engineer&l=New+York%2C+NY&vjk=67f4c335f087a0eb")
    driver.find_element(By.TAG_NAME, 'html')
    return driver.page_source

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  html_string = get_indeed_html(position = position, location = location, start = start)
  soup = bs(html_string, 'html.parser')
  tds = soup.find_all('td', {'class': 'resultContent'})
  return tds
  
  

  