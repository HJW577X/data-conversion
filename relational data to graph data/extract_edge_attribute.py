import re

ary = []
label = 1
path = 'graph.json'
rule = r':(.*?),'
fu_rule = r'"(.*?)"'
outfile=open('edge_relation.txt', 'w', encoding='utf-8')
with open(path, 'r', encoding='utf-8')as f:
    for line in f:
        if "start_id" in line:
            slotlist = re.findall(rule, line)
            if len(slotlist) > 2:
                slotlist[2] = slotlist[2].strip('}')
            else:
                slotlist.append('1')
            if label == 1:
                if slotlist[0] not in ary:
                    ary.append(slotlist[0])
                if slotlist[1] not in ary:
                    ary.append(slotlist[1])
                outfile.write(slotlist[0]+'\t'+slotlist[1]+'\t'+slotlist[2]+'\n')

print(ary)
print(len(ary))

outfile=open('entity_attribute.txt', 'w', encoding='utf-8')
with open(path, 'r', encoding='utf-8')as f:
    for line in f:
        if "id" in line and "start_id" not in line:
            slotlist = re.findall(rule, line)
            if slotlist[0] in ary:
                outfile.write(slotlist[0]+'\t'+slotlist[1]+'\t')
                fu_slotlist = re.findall(fu_rule, line)
                if len(fu_slotlist) == 5:
                    outfile.write(fu_slotlist[4]+'\n')
                elif len(fu_slotlist) == 9:
                    outfile.write(fu_slotlist[4]+'\t'+fu_slotlist[6]+'\t'+fu_slotlist[8]+'\n')
                else:
                    print(fu_slotlist)

