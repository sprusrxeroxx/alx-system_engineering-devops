#!/usr/bin/python3
""""
Python script that, uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    user_id = sys.argv[1]
    user = [user for user in data if user.get('id') == int(user_id)][0]
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = response.json()
    tasks = [task for task in data if task.get('userId') == int(user_id)]
    completed = [task for task in tasks if task.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed), len(tasks)))
    [print('\t {}'.format(task.get('title'))) for task in completed]