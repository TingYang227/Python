import json

name_emb = {'a': 1111,
            'b': 2222,
            'c': 3333,
            'd': None}

jsonObj = json.dumps(name_emb)

print(name_emb)

print(jsonObj)

print(type(name_emb))

print(type(jsonObj))