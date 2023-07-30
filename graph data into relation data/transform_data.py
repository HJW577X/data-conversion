import json
import random

ary = []
left = []
right = []
def read_ground_truth():
    i = 1
    with open("ground_truth.txt", 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            if len(line) > 0:
                if i % 2 != 0:
                    left.append(line)
                    i += 1
                else:
                    right.append(line)
                    i += 1
    for i in range(len(left)):
        ary.append([left[i], right[i]])
    print(ary)

def input_data():
    data = open('graph.json', 'r', encoding='utf-8')
    data = json.load(data)
    # print(data)
    outfile = open('train.txt', 'w', encoding='utf-8')
    pos = int(len(ary)/5 * 3)
    nag = 9 * pos
    count_nag = 0
    for i in range(len(ary)):
        # for train:
        # negative:
        for m in range(nag):
            if count_nag < nag:
                random_left = random.randint(45, 2201)
                random_right = random.randint(2486, 2687)
                if [str(random_left), str(random_right)] not in ary:
                    for n in data['Vertices']:
                        if n['id'] == random_left:
                            if n['entity_type'] != 2:
                                for z in n['properties']:
                                    if str(z) != 'id':
                                        outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                                outfile.write('\t')
                            else: break
                        if n['id'] == random_right:
                            for z in n['properties']:
                                if str(z) != 'id':
                                    outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                            outfile.write('\t' + str(0) + '\n')
                    count_nag += 1
                    # if random.randint(0, 3) == 3:
                    #     break
        #postive
        if i >= 0 and i < pos:
            print(i)
            for j in data['Vertices']:
                if j['id'] == int(left[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t')
                if j['id'] == int(right[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t' + str(1) + '\n')

    outfile = open('valid.txt', 'w', encoding='utf-8')
    pos_valid = int(len(ary)/5 * 4)
    nag_valid = 9 * (pos_valid - pos)
    count_nag = 0
    for i in range(len(ary)):
        # for train:
        # negative:
        for m in range(nag_valid):
            if count_nag < nag_valid:
                random_left = random.randint(45, 2201)
                random_right = random.randint(2486, 2687)
                if [str(random_left), str(random_right)] not in ary:
                    for n in data['Vertices']:
                        if n['id'] == random_left:
                            if n['entity_type'] != 2:
                                for z in n['properties']:
                                    if str(z) != 'id':
                                        outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                                outfile.write('\t')
                            else: break
                        if n['id'] == random_right:
                            for z in n['properties']:
                                if str(z) != 'id':
                                    outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                            outfile.write('\t' + str(0) + '\n')
                    count_nag += 1
                    # if random.randint(0, 2) == 2:
                    #     break
        #postive
        if i >= pos and i < pos_valid:
            print(i)
            for j in data['Vertices']:
                if j['id'] == int(left[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t')
                if j['id'] == int(right[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t' + str(1) + '\n')

    outfile = open('test.txt', 'w', encoding='utf-8')
    pos_test = int(len(ary)/5 * 5)
    nag_test = 9 * (pos_test - pos_valid)
    count_nag = 0
    for i in range(len(ary)):
        # for train:
        # negative:
        for m in range(nag_test):
            if count_nag < nag_test:
                random_left = random.randint(45, 2201)
                random_right = random.randint(2486, 2687)
                if [str(random_left), str(random_right)] not in ary:
                    for n in data['Vertices']:
                        if n['id'] == random_left:
                            if n['entity_type'] != 2:
                                for z in n['properties']:
                                    if str(z) != 'id':
                                        outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                                outfile.write('\t')
                            else: break
                        if n['id'] == random_right:
                            for z in n['properties']:
                                if str(z) != 'id':
                                    outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(n['properties'][str(z)]) + ' ')
                            outfile.write('\t' + str(0) + '\n')
                    count_nag += 1
                    # if random.randint(0, 2) == 2:
                    #     break
        #postive
        if i >= pos_valid and i < pos_test:
            print(i)
            for j in data['Vertices']:
                if j['id'] == int(left[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t')
                if j['id'] == int(right[i]):
                    for z in j['properties']:
                        if str(z) != 'id':
                            outfile.write("COL" + ' ' + str(z) + ' ' + "VAL" + ' ' + str(j['properties'][str(z)]) + ' ')
                    outfile.write('\t' + str(1) + '\n')


read_ground_truth()
input_data()
