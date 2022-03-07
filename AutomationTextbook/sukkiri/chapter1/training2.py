
scores = []
japanese = int(input('国語の点数：'))
scores.append(japanese)
math = int(input('数学の点数：'))
scores.append(math)
english = int(input('英語の点数：'))
scores.append(english)

print(scores)

total = sum(scores)

print(total)


