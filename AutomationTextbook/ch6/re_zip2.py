import re

with open('address.txt','rt',encoding='utf-8') as f:
    text = f.read()

pattern = r'〒(\d{3})-(\d{4})'
for m in re.finditer(pattern, text):
    print('---')
    print('場所：',m.span())
    print('全体：', m.group(0))
    print('前半：', m.group(1))
    print('後半：', m.group(2))