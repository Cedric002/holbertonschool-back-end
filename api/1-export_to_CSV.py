#!/usr/bin/python3


"Returns information employee ID"
"Export in CSV format method"


import csv
import requests
import sys


def export_employee_todo_list(employee_id):

    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')

    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                             task.get('completed'), task.get('title')])


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    export_employee_todo_list(employee_id)
