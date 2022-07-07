dict1 = {
    "value":11
}

dict2 = dict1

print("Before dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

dict2['value'] = 22

print("After dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)