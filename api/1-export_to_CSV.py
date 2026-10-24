#!/usr/bin/python3
""" Export the data from the previous task in CSV format.
"""
# ---- task 0 + new task ----
import csv
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
            USERNAME = name['name']
# counting the tasks done over the total tasks and export it in a csv format
    with open("USER_ID.csv", "w") as f:
        for todo in todos:
            if todo['userId'] == employee_id:
                USER_ID = todo['userId']
                TASK_COMPLETED_STATUS = todo['completed']
                TASK_TITLE = todo['title']
                print('"{}", "{}", "{}", "{}"'.format(
                    USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                    TASK_TITLE), file=f)
