#!/usr/bin/python3


"Returns all tasks of all employees"
"Export in JSON format method"


import json
import requests
import sys


def export_all_employees_todo_list():

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    all_data = {}

    for user in users_data:
        employee_id = user.get('id')
        employee_name = user.get('username')

        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        todos_data = todos_response.json()

        all_data[employee_id] = [
            {
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data
        ]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_data, file, indent=4)


if __name__ == "__main__":

    export_all_employees_todo_list()
