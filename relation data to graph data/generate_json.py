outfile = open('graph.json', 'w', encoding='utf-8')
outfile.write('{' + '\n')
outfile.write("\"Vertices\":[" + '\n')
with open('restaurant.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        item = '\t' + '{' + "\"id\"" + ':' + line[0] + ',' + "\"entity_type\"" + ':' + '0' + ',' + "\"properties\"" + ":{" + "\"name\"" + ':' + '\"' + line[2] + '\"' + ',' + "\"phone\"" + ':' + "\"" + line[3] + "\"" + ',' + "\"type\"" + ':' + "\"" + line[4] + "\"" + "}},"
        outfile.write(item + '\n')
with open('address.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        item = '\t' + '{' + "\"id\"" + ':' + line[0] + ',' + "\"entity_type\"" + ':' + '1' + ',' + "\"properties\"" + ":{" + "\"addr\"" + ':' + '\"' + line[1] + '\"'  + "}},"
        outfile.write(item + '\n')
with open('city.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        item = '\t' + '{' + "\"id\"" + ':' + line[0] + ',' + "\"entity_type\"" + ':' + '2' + ',' + "\"properties\"" + ":{" + "\"city\"" + ':' + '\"' + line[1] + '\"'  + "}},"
        outfile.write(item + '\n')
outfile.write("]," + '\n')
outfile.write("\"Edges\":[" + '\n')
with open('restaurant-address.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        edge = '\t' + '{' + "\"start_id\"" + ':' + line[0] + ',' + "\"target_id\"" + ':' + line[1] + ',' + "\"relationship_type\"" + ':' + '0' + "},"
        outfile.write(edge + '\n')
with open('address-city.txt', 'r', encoding='utf-8')as f:
    for line in f:
        line = line.strip('\n').split('\t')
        edge = '\t' + '{' + "\"start_id\"" + ':' + line[0] + ',' + "\"target_id\"" + ':' + line[1] + ',' + "\"relationship_type\"" + ':' + '1' + "},"
        outfile.write(edge + '\n')
outfile.write(']' + '\n')
outfile.write('}')