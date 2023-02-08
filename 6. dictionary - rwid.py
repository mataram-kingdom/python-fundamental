users = {
    "id" : "1",
    "name" : "muhammad afrizal",
    "username" : "zale",
    "email" : "hohohoho",
    "address" : {
        "desa" : "rejosa",
        "kec" : "pakis",
        "kab" : "magel",
    }
}
print(users)
print(users['name'])
print(users['username'])
print(users['email'])
print(users['id'])
print(users['address']['kab'])

print(users)
print(type(users))
print("\n ubah dictionary ke json")

import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json', 'w') as file :
    json.dump(users,file)