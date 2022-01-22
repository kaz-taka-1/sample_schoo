from bs4 import BeautifulSoup

with open('fish.html',encoding='utf-8') as fp:
    html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

res = []
div_list = soup.select('#fishes > div')
for div in div_list:
    fish = div.h2.text
    desc = div.select('.desc')[0].text
    price = div.select('.price')[0].text
    print(fish, desc, price)
    res.append([fish, desc, price])

import csv
with open('fish_csv', 'wt', encoding='sjis', newline='') as fp:
    csv.writer(fp).writerows(res)