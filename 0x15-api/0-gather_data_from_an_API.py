#!/usr/bin/python3
'''
This Python script uses specified REST API to return info about an employee's
TODO list progress given their employee ID
'''

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    x = requests.get(url+argv[1])
    name = x.json()['name']
    completed = []
    complete = 0
    incomplete = 0
    todos = requests.get(url+argv[1]+'/todos')
    for item in todos.json():
        if item['completed'] is True:
            complete += 1
            completed.append(item['title'])
        elif item['completed'] is False:
            incomplete += 1
    total = complete + incomplete
    print("Employee {} is done with tasks({}/{}):".format(name, complete, total
                                                          ))
    for task in completed:
        print('\t '+task)
