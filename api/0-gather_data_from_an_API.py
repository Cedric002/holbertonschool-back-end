#!/usr/bin/python3
"Returns information employee ID"

import requests  # type: ignore


def todo_list_progress(employee_id):

    employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos').json()

    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    employee_name = employee['name']

    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')

    for todo in todos:
        if todo['completed']:
            print('\t ' + todo['title'])


if __name__ == "__main__":

    todo_list_progress(1)
