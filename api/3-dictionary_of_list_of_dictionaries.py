#!/usr/bin/python3

"Returns information employee ID"
"Export in JSON format method"

import json
import requests


def todo_list_progress(employee_id):

    base_url = 'https://jsonplaceholder.typicode.com/users'
    all_users = requests.get(base_url).json()
    all_tasks = {}

    for user in all_users:
        employee_id = user['id']
        employee_name = user['name']
        todos = requests.get(f'{base_url}/{employee_id}/todos').json()
        tasks = []

        for todo in todos:
            task = {"username": employee_name, "task": todo['title'],
                    "completed": todo['completed']}
            tasks.append(task)
        all_tasks[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":

    todo_list_progress()
