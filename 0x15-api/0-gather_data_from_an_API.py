#!/usr/bin/python3
'''
This Python script uses specified REST API to return info about an employee's
TODO list progress given their employee ID
'''

import requests
from sys import argv

if __name__ == "__main__":
    users = 'https://jsonplaceholder.typicode.com/users/'
    todos = 'https://jsonplaceholder.typicode.com/todos/'
    x = requests.get(users+argv[1])
    name = x.json()['name']
    completed = []
    complete = 0
    incomplete = 0
    to_dos = requests.get(todos)
    for item in to_dos.json():
        if item['userId'] == int(argv[1]):
            if item['completed'] is True:
                complete += 1
                completed.append(item['title'])
            elif item['completed'] is False:
                incomplete += 1
    total = complete + incomplete
    print("Employee {} is done with tasks({}/{}):".format(name, complete, total
                                                          ))
    for task in completed:
        print('\t'+" "+task)
