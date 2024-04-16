#!/usr/bin/python3

import json
import requests

"Returns all tasks of all employees"
"Export in JSON format method"


def export_all_employees_todo_list():

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_tasks = {}
    for user in users_data:
        user_tasks = [
            {
                "username": user.get('name'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data if task.get('userId') == user.get('id')
        ]
        all_tasks[user.get('id')] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_employees_todo_list()
