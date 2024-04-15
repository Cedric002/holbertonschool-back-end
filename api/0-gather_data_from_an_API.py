#!/usr/bin/python3
"Returns information employee ID"

import requests
import sys


def get_employee_todo_list(employee_id):

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')

    done_tasks = [task for task in todos_data if task.get('completed')]

    print(f'Employee {employee_name} is done with tasks'
          f'({len(done_tasks)}/{len(todos_data)}):')

    for task in done_tasks:
        print('\t ' + task.get('title'))


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
