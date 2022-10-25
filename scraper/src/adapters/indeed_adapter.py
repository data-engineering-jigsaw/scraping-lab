from src.adapters.indeed_client import *
from src.models.position import Position
import requests
import re
import pdb

class IndeedAdapter:
    def __init__(self, card):
        self.card = card
        
    def get_id(self):
        return self.card.find('a')['data-jk']
    
    def get_title(self):
        return self.card.find('h2').text

    def get_salaries(self):
        salary = self.card.find('div', {'class': 'salary-snippet-container'})
        return salary.text

    def get_company_name(self):
        company = self.card.find('span', {'class': 'companyName'})
        return company.text
        
    def get_city_state(self):
        city_state = self.card.find('div', {'class': 'companyLocation'}).text
        split_text = city_state.split(', ')
        city = split_text[0]
        state = split_text[1].split()[0]
        return (city, state)

    def clean_salaries(self):
        salaries = self.get_salaries()
        first_salary, second_salary = salaries.split(' - ')
        cleaned_first = int(first_salary.replace('$', ''))
        cleaned_second = int(second_salary.split()[0].replace('$', ''))
        return [cleaned_first, cleaned_second]


    def run(self):
        id = self.get_id()
        title = self.get_title()
        clean_salaries = self.clean_salaries()
        company_name = self.get_company_name()
        city, state = self.get_city_state()
        return Position(id, title, clean_salaries, company_name, city, state)

    