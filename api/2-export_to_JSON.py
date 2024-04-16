#!/usr/bin/python3


"Returns information employee ID"
"Export in JSON format method"

import json
import requests
import sys


def export_employee_todo_list(employee_id):

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')

    tasks = [
        {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        } for task in todos_data
    ]

    print(f'Employee {employee_name} has {len(tasks)} tasks:')

    for task in tasks:
        print('\t ' + task.get('task'))

    return {str(employee_id): tasks}

if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    employee_tasks = export_employee_todo_list(employee_id)

    with open(f"{employee_id}.json", "w") as f:
        json.dump(employee_tasks, f, indent=4)
