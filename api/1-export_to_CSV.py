#!/usr/bin/python3
"Returns information employee ID"

import csv
import json
import requests
import sys


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

    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([employee_id, employee_name,
                             todo['completed'], todo['title']])
            if todo['completed']:
                print('\t ' + todo['title'])


if __name__ == "__main__":

    todo_list_progress(1)
