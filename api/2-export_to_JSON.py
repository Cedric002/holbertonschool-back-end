#!/usr/bin/python3


"Returns information employee ID"
"Export in JSON format method"


import json
import requests
import sys


def export_api(user_id):
    url_users = 'https://jsonplaceholder.typicode.com/users/' + user_id

    response = requests.get(url_users)
    if (response.ok):
        jData = json.loads(response.content)
        EMPLOYEE_NAME = jData["username"]
    else:
        response.raise_for_status()

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': user_id}

    response = requests.get(url_todos, params=query)
    if (response.ok):
        jData = json.loads(response.content)

        tasks = []
        for task in jData:
            tasks.append({
                "task": task.get("title"), "completed": task.get("completed"),
                "username": EMPLOYEE_NAME
            })

        with open("{}.json".format(user_id), "w") as json_file:
            json.dump({user_id: tasks}, json_file)
    else:
        response.raise_for_status()


if __name__ == "__main__":

    export_api(sys.argv[1])