#!/usr/bin/python3
import requests
import sys

id = int(sys.argv[1])

URL = 'https://jsonplaceholder.typicode.com/todos/'
URL_1 = 'https://jsonplaceholder.typicode.com/users/' 
response = requests.get(URL)
todos = response.json()
response_1 = requests.get(URL_1)
name = response_1.json()

tasks_done = 0
total_tasks = len(todos)
print(total_tasks)

 for id in todos[]:
     if todos['id'] == id:
         if todos.get('completed'):
             tasks_done += 1
         



#     print

# URL = f'https://jsonplaceholder.typicode.com'
# response = requests.get(URL)
# data = response.json()

#if user == 1:
 #   print(data[0]['id'])
    #print(data[0]['title'])
 #   tasks= data[0]['completed']
 #   n = 0
 #   s = 0
 #   if tasks is 'true':
 #       n+=1
 #   else:
 #       s+=1
 #   r = n + s
    #print(f'Employee {user} is done with tasks({n}/{r})')
    #print(f'EMPLOYEE_NAME: {user}')
   # print(f'NUMBER_OF_DONE_TASKS: {n}')
  #  print(f'TOTAL_NUMBER_OF_TASKS: {r}')
