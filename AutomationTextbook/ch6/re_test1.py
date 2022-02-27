import re

target = r'app dog art pot'
pattern = r'a..'
a = re.findall(pattern, target)

print(a)