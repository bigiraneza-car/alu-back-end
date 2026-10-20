import requests
user_id = 1

URL = f'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(URL)
data = response.json()
user = data[0]['userId']
# for user in data['userId': 1]:
#     print

# URL = f'https://jsonplaceholder.typicode.com'
# response = requests.get(URL)
# data = response.json()

if user == 1:
    print(data[0]['id'])
    print(data[0]['title'])
    tasks= data[0]['completed']
    n = 0
    s = 0
    if tasks is 'true':
        n+=1
    else:
        s+=1
    r = n + s
    print(f'Employee {user} is done with tasks({n}/{r})')
    print(f'EMPLOYEE_NAME: {user}')
    print(f'NUMBER_OF_DONE_TASKS: {n}')
    print(f'TOTAL_NUMBER_OF_TASKS: {r}')
