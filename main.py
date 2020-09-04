import csv

with open('data.csv', mode='r') as csv_file:
    data = csv.DictReader(csv_file)
    count = 0
    sum = 0
    for row in data:
        item_amt = float(row['order_amount']) / float(row['total_items'])
        sum += item_amt
        count += 1

    print(sum/count)