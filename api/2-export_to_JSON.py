#!/usr/bin/python3
""" Export data to JSON format.
"""
# ---- Task o + task 2 ----
import json
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
# Getting the tasks and the name of the employee
    URL = 'https://jsonplaceholder.typicode.com/todos/'
    URL_1 = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(URL)
    todos = response.json()
    response_1 = requests.get(URL_1)
    names = response_1.json()
# Finding the name of the employee
    for name in names:
        if name['id'] == employee_id:
            USERNAME = name['username']
# export all the tasks of the employee
    tasks = []
    for todo in todos:
        if todo['userId'] == employee_id:
            TASK_TITLE = todo['title']
            USER_ID = todo['userId']
            TASK_COMPLETED_STATUS = todo['completed']
            tasks.append({"task": TASK_TITLE, 
                          "completed": TASK_COMPLETED_STATUS, 
                          "username": USERNAME,
                          })
    data = {str(employee_id): tasks}
    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)
