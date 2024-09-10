import json


obj = open("data/ages.csv", "r")

d = {}

headers = obj.readline()

for name in headers:
     d{name} = []


