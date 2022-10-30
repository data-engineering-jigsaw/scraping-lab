from bs4 import BeautifulSoup as bs
from src.adapters.indeed_client import *
import pdb


def test_get_indeed_html():
    results = get_indeed_html(position = 'data engineer', location = 'United States', start = 1)
    html_str = '<!DOCTYPE html>\n<html dir="ltr" lang="en">\n<head>\n    <link rel="shortcut icon" href="/images/favicon.ico">'
    assert results.startswith(html_str)

def test_all_cards_are_td():
    tds = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    list(set([td.name == 'td' for td in tds])) == 'td'

