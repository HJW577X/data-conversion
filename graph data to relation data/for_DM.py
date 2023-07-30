import re
import csv
rule = r"VAL (.*?) COL"


ary = []
with open('test.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        line[0] = line[0].strip(' ')
        line[1] = line[1].strip(' ')
        ary.append(line)
id = 1527
outfile = open('test_DM.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(outfile)
csv_writer.writerow(["id", "label", "left_dob", "left_name", "right_dob", "right_name"])
# outfile.write("id,label,left_altitude,left_city,left_descr,right_altitude,right_city,right_descr" + '\n')
for i in range(len(ary)):
    # outfile.write(str(id) + ',' + str(ary[i][2] + ','))
    line_left = re.findall(rule, ary[i][0])
    # outfile.write(line_left[0] + ',' + line_left[1] + ',')
    line_left_last = ary[i][0].replace('VAL', '\t').split('\t')[2].strip(' ')
    # outfile.write(line_left_last + ',')
    print(i)
    line_right = re.findall(rule, ary[i][1])
    # outfile.write(line_right[0] + ',' + line_right[1] + ',')
    line_right_last = ary[i][1].replace('VAL', '\t').split('\t')[2].strip(' ')
    # outfile.write(line_right_last + '\n')
    csv_writer.writerow([str(id), str(ary[i][2]), line_left[0], line_left_last, line_right[0], line_right_last])
    id += 1
