#!/usr/bin/python3
""" Display the employee TODO list progress using a REST API.

Takes the employee ID as a command line argument and prints the number of tasks done over the total number of tasks of that employee followed by the title of the tasks completed.
"""
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    #Getting the tasks and the name of the employee
    URL = 'https://jsonplaceholder.typicode.com/todos/'
    URL_1 = 'https://jsonplaceholder.typicode.com/users/' 
    response = requests.get(URL)
    todos = response.json()
    response_1 = requests.get(URL_1)
    names = response_1.json()
    #Finding the name of the employee
    for name in names:
        if name['id'] == employee_id:
            EMPLOYEE_NAME = name['name']
    #counting the tasks done over the total tasks
    NUMBER_OF_DONE_TASKS = 0
    TASKS_NOT_DONE = 0

    for todo in todos:
        if todo['userId'] == employee_id:
            if todo.get('completed'):
                NUMBER_OF_DONE_TASKS += 1

            else:
                TASKS_NOT_DONE += 1
    TOTAL_NUMBER_OF_TASKS = NUMBER_OF_DONE_TASKS + TASKS_NOT_DONE
    #printing the results in the exact following format
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for todo in todos:
        if todo['userId'] == employee_id:
            if todo.get('completed'):
                TASK_TITLE = todo['title']
                print('         {}'.format(TASK_TITLE))
