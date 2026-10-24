#!/usr/bin/python3
""" Export all tasks to json.
"""
import json
import requests
if __name__ == "__main__":
    # Getting the tasks and the name of the employee
    URL = 'https://jsonplaceholder.typicode.com/todos/'
    URL_1 = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(URL)
    todos = response.json()
    response_1 = requests.get(URL_1)
    names = response_1.json()
    # Getting all records for all employees
    data = {}
    for name in names:
        tasks = []
        for todo in todos:
            if name['id'] == todo['userId']:
                USERNAME = name['username']
                TASK_TITLE = todo['title']
                USER_ID = todo['userId']
                TASK_COMPLETED_STATUS = todo['completed']
                tasks.append({
                    "username": USERNAME,
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS,
                            })
        data[str(name['id'])] = tasks

    # Exporting them in a json format
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
