#!/usr/bin/python3
"Returns information employee ID"

import requests


def todo_list_progress(employee_id):

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee = requests.get(url).json()

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos = requests.get(url).json()

    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    employee_name = employee['name']

    print(f'Employee {employee_name} is done with tasks'
          f'({done_tasks}/{total_tasks}):')

    for todo in todos:
        if todo['completed']:
            print('\t ' + todo['title'])


if __name__ == "__main__":

    todo_list_progress(1)
