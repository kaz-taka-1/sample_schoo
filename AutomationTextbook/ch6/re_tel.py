import re
tel = r'[電話]000-1111-2222'

pattern = r'(\d+)-(\d+)-(\d+)'
rep=r'(\1) \2 - \3'
print(re.sub(pattern, rep, tel))