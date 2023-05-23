#!/usr/bin/python3
'''
This Python script uses specified REST API to generate CSV file with
info about an employee's TODO list given the employee's ID
'''

import vsv
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
    CSV_out = argv[1] + '.csv'
    with open(CSV_out, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in todos.json():
            write.writerow([argv[1], name, i.get('completed'), i.get('title')])
