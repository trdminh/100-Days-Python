import csv2
import json

json_str = '{"name": "Minh", "age": 20, "title": "student"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)