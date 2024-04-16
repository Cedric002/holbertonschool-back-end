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

    done_tasks = [task for task in todos_data if task.get('completed')]

    print(f'Employee {employee_name} is done with tasks'
          f'({len(done_tasks)}/{len(todos_data)}):')

    csv_data = [(user_data['id'], user_data['name'],
                 task['completed'], task['title']) for task in todos_data]

    csv_filename = f"{user_data['id']}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["USER_ID",
                            "USERNAME",
                            "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])
        csvwriter.writerows(csv_data)

    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    export_employee_todo_list(employee_id)
