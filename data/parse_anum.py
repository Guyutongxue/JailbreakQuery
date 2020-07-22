import re
import json
from typing import List, Dict

f = open('model.mediawiki', 'r')
data: Dict[str, str] = {}
anum: List[str] = []
identifier: ''
for line in f.readlines():
    if re.match('^\|', line) is None:
        continue
    line = re.sub('^\|[^|]+?\|', '|', line)
    line = re.sub('<\s*?br\s*?/?>', ',', line)
    line = re.sub('<.*?/?>', '', line)
    line = re.sub('\(.*?\)', '', line)
    matchObj = re.match('^\| (A\d{4}\s?(,A\d{4}\s?)*)$', line)
    if matchObj is not None:
        temp = matchObj.group(1).strip('\n').split(',')
        anum = [i.strip() for i in temp]
        #print(anum)
        #input()
        continue
    nextMatch = re.match('^\| ([A-Za-z]+\d+,\d+)$', line)
    if nextMatch is not None:
        identifier = nextMatch.group(1).strip('\n')
        #print(identifier)
        #input()
        for i in anum:
            data[i] = identifier
        if len(anum) == 0:
            print(identifier)
        anum = []
    if re.match('^\|-', line) is not None:
        for i in anum:
            data[i] = identifier
        anum = []

f.close()
del f

# patch: TIW not updated yet
# iPad Pro 12.6 4G
data['A2068'] = 'iPad8,11'
data['A2228'] = 'iPad8,11'
data['A2230'] = 'iPad8,11'
data['A2231'] = 'iPad8,11'
# iPad Pro 11 2G
data['A2069'] = 'iPad8,9'
data['A2229'] = 'iPad8,9'
data['A2232'] = 'iPad8,9'
data['A2233'] = 'iPad8,9'
# iPhone SE 2G
data['A2275'] = 'iPhone12,8'
data['A2296'] = 'iPhone12,8'
data['A2298'] = 'iPhone12,8'

# [{'identifier': key, 'models': value} for key, value in data.items()]

with open('model.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
