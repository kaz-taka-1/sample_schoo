height = int(input('身長(cm)を入力して下さい'))
weight = int(input('体重(kg)を入力して下さい'))

height = height / 100

bmi = weight / (height ** 2)

print('あなたのbmiは{}'.format(bmi))


