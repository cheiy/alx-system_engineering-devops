#!/usr/bin/python3
'''
This Python script uses specified REST API to return info about an employee's
TODO list progress given their employee ID
'''


import requests
from sys import argv
import json

if __name__ == "__main__":

    session = requests.Session()
    EmpId = argv[1]
    todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(EmpId)
    names = 'https://jsonplaceholder.typicode.com/users/{}'.format(EmpId)

    employee = session.get(todos)
    employeeName = session.get(names)

    json_request = employee.json()
    name = employeeName.json()['name']
    complete = 0

    for tasks in json_request:
        if tasks['completed']:
            complete += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, complete, len(json_request)))

    for complete in json_request:
        if complete['completed']:
            print("\t " + complete.get('title'))
