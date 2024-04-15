#!/usr/bin/python3

"Returns information employee ID"
"Export in CSV format method"
"Export in JSON format method"

import csv
import requests


def todo_list_progress(employee_id):

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee = requests.get(url).json()

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos = requests.get(url).json()

    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])

    print(f'Employee {employee["name"]} is done with tasks'
          f'({done_tasks}/{total_tasks}):')
    tasks = []

    for todo in todos:
        task = {"task": todo['title'], "completed": todo['completed'],
                "username": employee["name"]}
        tasks.append(task)

        if todo['completed']:
            print('\t ' + todo['title'])

    with open(f'{employee_id}.json', 'w') as file:
        json.dump({employee_id: tasks}, file)


if __name__ == "__main__":

    todo_list_progress(1)
