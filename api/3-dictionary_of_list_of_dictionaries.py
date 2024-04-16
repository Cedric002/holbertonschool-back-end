#!/usr/bin/python3


"Returns all tasks of all employees"
"Export in JSON format method"


import json
import requests
import sys


def export_all_employees_todo_list():

    user_response = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user_response.json()

    all_employee_tasks = {}

    for user in user_data:
        user_id = user['id']
        username = user['username']
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
        todos_data = todos_response.json()

        employee_tasks = []
        for task in todos_data:
            employee_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        all_employee_tasks[user_id] = employee_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employee_tasks, f, indent=4)

    print("Data exported to 'todo_all_employees.json'")


if __name__ == "__main__":

    export_all_employees_todo_list()
