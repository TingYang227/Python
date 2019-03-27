import json

python_obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)},True,False,None]

print(python_obj)

json_str = json.dumps(python_obj)

print(json_str)

python_obj2 = {"key2": [4, 5, 6], "key1": [1, 2, 3]}
json_str2 = json.dumps(python_obj2, indent=2)

print(json_str2)