import sys
import json
import shutil

file1 = "task3/" + sys.argv[1]
file2 = "task3/" + sys.argv[2]

with open(file1, 'r') as file:
    tests_data = json.load(file)

with open(file2, 'r') as file:
    values_data = json.load(file)

def update_tests(tests, values):
    for test in tests:
        for value in values:
            if value['id'] == test['id']:
                test['value'] = value['value']
        if 'values' in test:
            update_tests(test['values'], values)

update_tests(tests_data['tests'], values_data['values'])

with open('report.json', 'w') as file:
    json.dump(tests_data, file, indent=4)
shutil.move('report.json', 'task3/report.json')
