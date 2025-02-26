import json

from baseConverter import BaseConverter

with open("converter-base.json","r") as FileHandler:
    data = json.load(FileHandler)

print(data)
conv = BaseConverter(data)

val = conv.getValue()

print(val)