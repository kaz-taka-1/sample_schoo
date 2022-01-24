import os, requests, csv
from bs4 import BeautifulSoup

target_url = 'https://uta.pw/shodou/index/php?master'
save_file = 'meisaku.txt'

html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

res = []
for art in soup.select('.art_title'):
    art_titles = art.select('.art_title')
    if len(art_titles) < 2: continue
    title = art_titles[1].text
    src = art.select('img')[0]['src']
    res.append([title, src])
    print(title, src)

with open(save_file, 'wt', encoding='utf-8') as fp:
    csv.writer(fp, delimiter='\t').writerows(res)