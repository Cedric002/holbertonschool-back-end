#!/usr/bin/python3
"Returns information employee ID"

import urllib.request
import json


def todo_list_progress(employee_id):

    base_url = 'https://jsonplaceholder.typicode.com/users/'

    # Retrieves employee details
    with urllib.request.urlopen(f'{base_url}{employee_id}') as url:
        employee = json.loads(url.read().decode())

    # Retrieves the employee's todo list
    with urllib.request.urlopen(f'{base_url}{employee_id}/todos') as url:
        todos = json.loads(url.read().decode())

    # Calculates progress
    total_tasks = len(todos)
    done_tasks = sum(todo.get('completed') for todo in todos)
    employee_name = employee.get('name')

    # Print progress
    print(f'Employee {employee_name} is done with tasks'
          f'({done_tasks}/{total_tasks}):')

    # Print completed tasks
    for todo in todos:
        if todo.get('completed'):
            print('\t ' + todo.get('title'))


if __name__ == "__main__":

    # Test the function with a sample employee ID
    todo_list_progress(1)
