#!/usr/bin/python3

"Returns information employee ID"
"Export in CSV format method"

import csv
import requests
import sys


def export_employee_todo_list(USER_ID):

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{USER_ID}')
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos')

    user_data = user_response.json()
    todos_data = todos_response.json()
    USERNAME = user_data.get('name')

    rows = [[USER_ID, USERNAME, task.get('TASK_COMPLETED_STATUS'),
             task.get('TASK_TITLE')]
            for task in todos_data]

    with open(f'{USER_ID}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)


if __name__ == "__main__":

    USER_ID = int(sys.argv[1])
    export_employee_todo_list(USER_ID)
