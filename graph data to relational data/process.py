import pandas as pd
import re
import csv

train = pd.read_csv('train.txt', sep='\t')
train = train.values.tolist()

valid = pd.read_csv('valid.txt', sep='\t')
valid = valid.values.tolist()

test = pd.read_csv('test.txt', sep='\t')
test = test.values.tolist()

table = train + valid + test

tableA = []
tableB = []

id_left = 0
id_right = 0

for i in range(len(table)):
    left_attribute = re.findall(r'VAL\ (.*?)\ COL', table[i][0])
    left_attribute.append(table[i][0].split(' ')[-2])
    if left_attribute not in tableA:
        tableA.append(left_attribute)

    right_attribute = re.findall(r'VAL\ (.*?)\ COL', table[i][1])
    right_attribute.append(table[i][1].split(' ')[-2])
    if right_attribute not in tableB:
        tableB.append(right_attribute)

for i in range(len(tableA)):
    tableA[i].insert(0, i)
for i in range(len(tableB)):
    tableB[i].insert(0, i)

with open("tableA.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    name = ['id', 'dob', 'name']
    csv_writer.writerow(name)
    csv_writer.writerows(tableA)

with open("tableB.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    name = ['id', 'dob', 'name']
    csv_writer.writerow(name)
    csv_writer.writerows(tableB)

train_id = []
for i in range(len(train)):
    left_attribute = re.findall(r'VAL\ (.*?)\ COL', train[i][0])
    left_attribute.append(train[i][0].split(' ')[-2])
    for j in range(len(tableA)):
        for k in range(len(left_attribute)):
            if left_attribute[k] not in tableA[j]:
                break
        if k == len(left_attribute) - 1:
            left_id = tableA[j][0]
            break

    right_attribute = re.findall(r'VAL\ (.*?)\ COL', train[i][1])
    right_attribute.append(train[i][1].split(' ')[-2])
    for j in range(len(tableB)):
        for k in range(len(right_attribute)):
            if right_attribute[k] not in tableB[j]:
                break
        if k == len(right_attribute) - 1:
            right_id = tableB[j][0]
            break
    train_id.append([left_id, right_id, train[i][2]])

with open("train.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    name = ['ltable_id', 'rtable_id', 'label']
    csv_writer.writerow(name)
    csv_writer.writerows(train_id)

valid_id = []
for i in range(len(valid)):
    left_attribute = re.findall(r'VAL\ (.*?)\ COL', valid[i][0])
    left_attribute.append(valid[i][0].split(' ')[-2])
    for j in range(len(tableA)):
        for k in range(len(left_attribute)):
            if left_attribute[k] not in tableA[j]:
                break
        if k == len(left_attribute) - 1:
            left_id = tableA[j][0]
            break

    right_attribute = re.findall(r'VAL\ (.*?)\ COL', valid[i][1])
    right_attribute.append(valid[i][1].split(' ')[-2])
    for j in range(len(tableB)):
        for k in range(len(right_attribute)):
            if right_attribute[k] not in tableB[j]:
                break
        if k == len(right_attribute) - 1:
            right_id = tableB[j][0]
            break
    valid_id.append([left_id, right_id, valid[i][2]])

with open("valid.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    name = ['ltable_id', 'rtable_id', 'label']
    csv_writer.writerow(name)
    csv_writer.writerows(valid_id)

test_id = []
for i in range(len(test)):
    left_attribute = re.findall(r'VAL\ (.*?)\ COL', test[i][0])
    left_attribute.append(test[i][0].split(' ')[-2])
    for j in range(len(tableA)):
        for k in range(len(left_attribute)):
            if left_attribute[k] not in tableA[j]:
                break
        if k == len(left_attribute) - 1:
            left_id = tableA[j][0]
            break

    right_attribute = re.findall(r'VAL\ (.*?)\ COL', test[i][1])
    right_attribute.append(test[i][1].split(' ')[-2])
    for j in range(len(tableB)):
        for k in range(len(right_attribute)):
            if right_attribute[k] not in tableB[j]:
                break
        if k == len(right_attribute) - 1:
            right_id = tableB[j][0]
            break
    test_id.append([left_id, right_id, test[i][2]])

with open("test.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    name = ['ltable_id', 'rtable_id', 'label']
    csv_writer.writerow(name)
    csv_writer.writerows(test_id)