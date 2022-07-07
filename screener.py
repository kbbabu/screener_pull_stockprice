import requests
page1 = requests.get('https://www.screener.in/company/WIPRO/consolidated/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page1.content,'html.parser')
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

dummy(page)
