scores = []

for i in range(10):
    score = int(input('{}人目の得点：'.format(i+1)))
    scores.append(score)

final_scores = []
for score in scores:
    data = 0.8 * score + 20
    final_scores.append(data)

average = 0
for data in final_scores:
    average = average + data

print(average)


