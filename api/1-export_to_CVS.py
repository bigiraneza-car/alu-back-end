#!/usr/bin/python3
""" Export the data from the previous task in CSV format.
"""
# ---- task 0 + new task ----
import requests
import sys
import csv

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
            EMPLOYEE_NAME = name['name']
# counting the tasks done over the total tasks and export it in a csv format
    with open("USER_ID.csv", "w") as f:
        for todo in todos:
            if todo['userId'] == employee_id:
                print('"{}", "{}", "{}", "{}"'.format(
                    todo['userId'], EMPLOYEE_NAME, todo['completed'],
                    todo['title']), file=f)

