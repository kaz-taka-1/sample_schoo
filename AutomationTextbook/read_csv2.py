import csv

with open('items2.csv', encoding='sjis') as f:
    reader = csv.reader(f)
    head = next(reader)

    total = 0
    for row in reader:
        name, price, cnt, subtotal = row
        print(name, price, cnt, subtotal)
        total += int(subtotal)
    print("合計:", total, "円")