import os
from pprint import pprint
current = os.getcwd()
result = os.listdir(current)
all_list = []
for file_name in os.listdir(current):
    if file_name.endswith('.txt'):
        file = open(file_name,'r', encoding='utf-8')
        res = file.readlines()
        res1 = len(res)
        #print(res1)

        element = {
            'file_name': file_name,
            'value1': res1,
            'value2': res
        }
        #pprint(element)
        all_list.append(element)
sorted_values = sorted(all_list ,key=lambda el: el['value1'])
#pprint(sorted_values)
file_ = open('4.txt', 'w', encoding='utf-8')
for line in all_list:
   file_.write(f"{line['file_name']}\n")
   file_.write(f"{line['value1']}\n")
   file_.write(f"{(''.join(line['value2']))}\n")


