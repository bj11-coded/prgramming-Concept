# object cannot be used directly without converting them into json so
# we use json module

# json is a syntex for storing and exchanging data
import json as j

# a python object / dictionary
data = {
    "name":"jhon",
    "klass": "Bachelor",
    "married":False,
    "cars":[
        {"model":"BMW 120", "color":"red"},
        {"model":"BYD Auto 3","color":"black"}
    ]

}

# dumps converts object into json Format
newJson = j.dumps(data)
print(newJson)


# to convet json into dictionary or object we use loads
jsn = '{"name":"bijay","klass":"bachelor"}'
convDict = j.loads(jsn)
print(convDict["name"])