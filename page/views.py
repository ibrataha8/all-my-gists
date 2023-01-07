from django.shortcuts import render
import json
import os
module_dir = os.path.dirname(__file__)
with open( os.path.join(module_dir, 'Data.txt'), 'r') as file:
  lines = file.readlines()
# print(list(map(strip,lines)))

#{'Key1':['V1','V2'],'Key2':['V1','V2']}
dic = {}
store_lines = False
header_stored = ''
lines_stored = []
for line in lines:
    #dic[line] = lines
    if line.endswith(':\n') :
        store_lines = True
        if len(lines_stored) != 0:
            dic[header_stored.strip(': ')] = lines_stored
            lines_stored = []
        header_stored = line.strip()
    elif store_lines == True:
        lin = line.strip()
        if lin != '':
            lines_stored.append(lin)
def index(request):
    return render(request,'page/index.html',{'data':dic})