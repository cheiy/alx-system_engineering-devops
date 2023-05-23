#!/usr/bin/python3
'''
This Python script uses specified REST API to generate CSV file with
info about an employee's TODO list given the employee's ID
'''


import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    x = requests.get(url+argv[1])
    u_n = x.json()['username']
    completed = []
    complete = 0
    incomplete = 0
    tasks = []
    update = {}
    todos = requests.get(url+argv[1]+'/todos')
    for item in todos.json():
        tasks.append(
                {
                    "task": item.get('title'),
                    "completed": item.get('completed'),
                    "username": u_n,
                    })
    update[argv[1]] = tasks
    json_f = argv[1]+'.json'
    with open(json_f, "w") as jsonfile:
        json.dump(update, jsonfile)
