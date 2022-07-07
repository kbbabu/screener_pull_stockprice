import requests
page = requests.get('https://www.screener.in/company/WIPRO/consolidated/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
def dummy(page):
  soup = BeautifulSoup(page.content,'html.parser')  
  c = soup.find('h1',{'class':'margin-0'})
  name = c.string
  d = soup.find('div',{'class':'company-ratios'})
  e = d.findAll('span')
  price = e[5].string
  mcap = e[2].string
  hprice_52week = e[8].string
  lprice_52week = e[9].string
  pe = e[12].string
  bookvalue =e[15].string
  div_yield =e[18].string
  ROCE =e[21].string
  ROE = e[24].string
  facevalue = e[27].string
  return (name,price,mcap,hprice_52week,lprice_52week,pe,bookvalue,div_yield,ROCE,ROE,facevalue)

print(dummy(page))

import pandas as pd
a = ['0','201-400','401-600','601-800','801-1000','1001-1200','1201-1400','1401-1600','1601-1800','1801-2000','2001-2200','2201-2400','2401-2600','2601-2800','2801-2900']
all_code = []
for i in a:
    all_code.append(f"https://money.rediff.com/companies/nseall/{i}")
all_code_values = []
for i in all_code:
    all_code_values.append(pd.read_html(i))
url_captured = []
for i in range(15):
    j = (all_code_values[i][1].Code.values)
    for z in j:
        url_captured.append(f"https://www.screener.in/company/{z}/consolidated/")
    j = (all_code_values[i][2].Code.values)
    for z in j:
        url_captured.append(f"https://www.screener.in/company/{z}/consolidated/")
lin = []
for i in url_captured:
  page = requests.get(i)
  lin.append(page)

dum = []
for i in lin:
  try:
    p = dummy(i)
    dum.append(p)
  except:
    pass
  
tot = pd.DataFrame(dum)
tot.to_excel("/screener_demo.xlsx")
