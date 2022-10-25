from bs4 import BeautifulSoup as bs
from src.adapters.indeed_adapter import *
import pdb

html_doc = """
<td class="resultContent"><div class="css-1m4cuuf e37uo190"><h2 class="jobTitle css-1h4a4n5 eu4oa1w0" tabindex="-1"><a id="sj_8cba12eacacdf624" data-mobtk="1gg7ukufnj30s801" data-jk="8cba12eacacdf624" data-ci="4120764" data-empn="5549280949310828" data-hiring-event="false" target="_blank" data-hide-spinner="true" role="button" aria-label="full details of Data Engineer" class="jcs-JobTitle css-jspxzf eu4oa1w0" href="/pagead/clk?mo=r&amp;ad=-6NYlbfkN0CE4oJ6ADOgzMo6rVWG1sja39QP9hSoep3-VANbPJrAxhmQQ9Er9BBE0PxZLipUtFjPDeM-Hw3Xx3oGFwmX85V-3iPZa7BeMiqJ47szn9MCgKVkO6dEJgOsprHCfWvLa02FZQS7nPpnXMvFM4VKwM49enQ5qRay5eVvc-j6gtCman6pkKZJxSb5Ny8vp-kU8zhvJe1cIkiAVFx8qmF3z2uO16QwyzefGGTirC-LSJGJJ1MccSKlVMyvwQtHgtmFEMCSh0UBH2Rbib5B9PN0LnCVC7zaW423sh0e6TpyOmwYjMB6Br1eM13MOshIRxnmU3CURuW-pHAmn0XifGa0XEWze4DIL4HGexAkBYtI5HEgLspNqxdJl7TyVUhq9WtF25u_lENitc-23Mbq4GGFvSFSrWEyDBD1dOM727aNjQOQG_db5q5EyBg7iuCdmlmbjF157jGWr3QEU-CHknEry8ZzrNfhpISITACQjj9YGUSUiQ==&amp;xkcb=SoC7-_M3XH1cDVwnK50LbzkdCdPP&amp;p=0&amp;fvj=1&amp;vjs=3&amp;tk=1gg7ukufnj30s801&amp;jsa=5735"><span title="Data Engineer" id="jobTitle-8cba12eacacdf624">Data Engineer</span></a></h2></div><div class="heading6 company_location tapItem-gutter companyInfo"><span class="companyName">Ana-Data Consulting Inc</span><div class="companyLocation">New York, NY 10469<!-- -->&nbsp;<span class="companyLocation--extras">(<!-- -->Pelham Gardens area<!-- -->)</span></div></div><div class="heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"><div class="metadata salary-snippet-container"><div class="attribute_snippet"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 13" role="presentation" aria-hidden="true" aria-label="Salary"><defs></defs><path fill="#595959" fill-rule="evenodd" d="M2.45168 6.10292c-.30177-.125-.62509-.18964-.95168-.1903V4.08678c.32693-.00053.6506-.06518.95267-.1903.30331-.12564.57891-.30979.81105-.54193.23215-.23215.4163-.50775.54194-.81106.12524-.30237.18989-.62638.19029-.95365H9.0902c0 .3283.06466.65339.1903.9567.12564.30331.30978.57891.54193.81106.23217.23215.50777.41629.81107.54193.3032.12558.6281.19024.9562.1903v1.83556c-.3242.00155-.6451.06616-.9448.19028-.3033.12563-.5789.30978-.81102.54193-.23215.23214-.4163.50774-.54193.81106-.12332.2977-.18789.61638-.19024.93849H3.99496c-.00071-.32645-.06535-.64961-.19029-.95124-.12564-.30332-.30979-.57891-.54193-.81106-.23215-.23215-.50775-.4163-.81106-.54193zM0 .589843C0 .313701.223858.0898438.5.0898438h12.0897c.2762 0 .5.2238572.5.5000002V9.40715c0 .27614-.2238.5-.5.5H.5c-.276143 0-.5-.22386-.5-.5V.589843zM6.54427 6.99849c1.10457 0 2-.89543 2-2s-.89543-2-2-2-2 .89543-2 2 .89543 2 2 2zm8.05523-2.69917v7.10958H2.75977c-.27615 0-.5.2238-.5.5v.5c0 .2761.22385.5.5.5H15.422c.4419 0 .6775-.2211.6775-.6629V4.29932c0-.27615-.2239-.5-.5-.5h-.5c-.2761 0-.5.22385-.5.5z" clip-rule="evenodd"></path></svg>$70 - $73 an hour</div></div><div class="metadata"><div class="attribute_snippet"><svg width="14" height="13" viewBox="0 0 14 13" fill="none" role="presentation" xmlns="http://www.w3.org/2000/svg" aria-label="Job type" aria-hidden="true"><path fill="#595959" fill-rule="evenodd" d="M4.50226.5c-.27614 0-.5.223858-.5.5v2.1H.5c-.276142 0-.5.22386-.5.5v1.9h14V3.6c0-.27614-.2239-.5-.5-.5h-3.4977V1c0-.276142-.22389-.5-.50004-.5h-5Zm4.19962 2.6H5.30344V1.8h3.39844v1.3Z" clip-rule="evenodd"></path><path fill="#595959" d="M5.70117 6.80005H0v5.20005c0 .2761.223857.5.5.5h13c.2761 0 .5-.2239.5-.5V6.80005H8.30117v.80322c0 .27614-.22386.5-.5.5h-1.6c-.27614 0-.5-.22386-.5-.5v-.80322Z"></path></svg>Contract</div></div><div class="metadata"><div class="attribute_snippet"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 15" role="presentation" aria-hidden="true" aria-label="Shift" height="15px"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 14.5C10.866 14.5 14 11.366 14 7.5C14 3.63401 10.866 0.5 7 0.5C3.13401 0.5 0 3.63401 0 7.5C0 11.366 3.13401 14.5 7 14.5ZM6.2496 4.25C6.2496 4.11193 6.36153 4 6.4996 4H7.2996C7.43767 4 7.5496 4.11193 7.5496 4.25V7.62406L9.62708 8.82349C9.74665 8.89252 9.78762 9.04542 9.71858 9.16499L9.31858 9.85781C9.24955 9.97739 9.09665 10.0184 8.97708 9.94932L6.25028 8.375H6.2496V8.37461L6.24805 8.37371L6.2496 8.37102V4.25Z" fill="#595959"></path></svg>8 hour shift</div></div></div><div class="heading6 error-text tapItem-gutter"></div></td>
"""
html_doc = bs(html_doc, 'html.parser')
card = html_doc.find('td')

def test_get_id_gets_id():
    indeed_adapter = IndeedAdapter(card)
    id = indeed_adapter.get_id()
    assert id == "8cba12eacacdf624"

def test_get_title():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_title() == "Data Engineer"

def test_get_salaries():
    indeed_adapter = IndeedAdapter(card)
    return indeed_adapter.get_salaries() == '$70 - $73 an hour'

def test_get_company_name():
    indeed_adapter = IndeedAdapter(card)
    assert indeed_adapter.get_company_name() == "Ana-Data Consulting Inc"

def test_get_city_state():
    indeed_adapter = IndeedAdapter(card)
    city, state = indeed_adapter.get_city_state()
    assert city == 'New York'
    assert state == 'NY'

def test_run_adapter_returns_instance_of_position():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    assert type(position) == Position

def test_run_adapter_returns_obj_with_correct_attributes():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_keys = ['id', 'title', 'salaries', 'city', 'state', 'company_name']
    keys = list(vars(position).keys())
    assert obj_keys == keys

def test_run_adapter_returns_obj_with_correct_values():
    indeed_adapter = IndeedAdapter(card)
    position = indeed_adapter.run()
    obj_vals = ['8cba12eacacdf624', 'Data Engineer', [70, 73], 'Ana-Data Consulting Inc', 'New York', 'NY']
    vals = list(vars(position).values())
    assert obj_vals == vals


    



