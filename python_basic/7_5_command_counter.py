# dictionary lab

import csv

def qetKey(item):
    return item[1]

command_data = []
with open("command_data.csv","r", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)


command_counter = {}

print(command_data[:10])
for data in command_data:
    print(data[0], data[1])
    if data[1] in command_counter.keys():
        command_counter[data[1]] +=1
    else:
        command_counter[data[1]] = 1

# print(command_counter)
