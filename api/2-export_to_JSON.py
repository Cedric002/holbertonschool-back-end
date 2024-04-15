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

    tasks = [{"task": task.get('title'), "completed":
              task.get('completed'), "username": employee_name}
             for task in todos_data]

    with open(f'{employee_id}.json', 'w') as file:
        json.dump({employee_id: tasks}, file)


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    export_employee_todo_list(employee_id)
