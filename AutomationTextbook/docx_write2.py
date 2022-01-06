import docx
import datetime

template_file = 'letter.docx'
save_file = 'letter-suzuki2.docx'
now = datetime.datetime.now()

card = {
    '2021年10月10日': now.strftime('%Y年%m月%d日'),
    '●●●御中': 'マイナビ出版御中',
    '■■■様': '鈴木様',
    '★★★の送付について': '契約書の送付について'
}
cstyle = {
    '★★★の送付について': True
}
doc = docx.Document(template_file)

for p in doc.paragraphs:
    for k,v in  card.items():
        if p.text.find(k) >= 0:
            p.text.replace(k, v)
            if k in  cstyle:
                font = p.runs[0].font
                font.bold = True
                font.underline = True
                font.size = docx.shared.Pt(20)

doc.save(save_file)