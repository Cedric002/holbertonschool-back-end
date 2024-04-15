#!/usr/bin/python3

import requests
import json
import sys

def todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    employee = requests.get(f'{base_url}/{employee_id}').json()
    todos = requests.get(f'{base_url}/{employee_id}/todos').json()
    tasks = []
    for todo in todos:
        task = {"username": employee["name"], "task": todo['title'],
                "completed": todo['completed']}
        tasks.append(task)
        
    with open(f'{employee_id}.json', 'w') as file:
        json.dump({employee_id: tasks}, file)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        todo_list_progress(sys.argv[1])
    else:
        print("Employee's ID")
