#!/usr/bin/env python
import json
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET

"""f = open("kafka_telemetry_output.json", "r")
dump = f.read().splitlines()
json_dump = json.load(f.read().splitlines())
json_dump = json.dumps(dump)
"""

#f = open('kafka_telemetry_output.json')
f = open('test1.json')
json_dump = (f.read())
f.close()


json_dump1 = json.loads(json_dump)
  
xml = dicttoxml(json_dump1)

#print(xml)
#print(json_dump1)
"""
for i in json_dump1:
    #if i is 'path':
        print(i)
        print(json_dump1[i])
        print(json_dump1[i]["elem"])
        for j in json_dump1[i]["elem"]:
            # print(j['key']['name'])
            print(j['name'])
"""
tree = (ET.fromstring(xml))
print(tree)

interface_name = tree.find("key/name")
print(interface_name.text)
item_name = tree.find("name")
print(item_name.text)
interface_status = tree.find("val/stringVal")
print(interface_status.text)
