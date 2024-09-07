import json
test_data=[{"name":"Tom","age":18},{"name":"Tom","age":18},{"name":"jerry","age":20},{"name":"Tony","age":12},{"name":"cici","age":28}]
json_data=json.dumps(test_data)
print(json_data)