import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
    url = 'http://www.indeed.com/jobs'
    params = {'q': position, 'l': location, 'explvl':'entry_level', 'start': start}
    response = requests.get(url, params = params, headers = headers, timeout=10)
    return response.text

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  html_string = get_indeed_html(position = position, location = location, start = start)
  soup = bs(html_string, 'html.parser')
  tds = soup.find_all('td', {'class': 'resultContent'})
  return tds
  
  

  