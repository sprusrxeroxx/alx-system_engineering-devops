#!/usr/bin/python3
""""
Python script that exports data from an API in CSV format.
"""
import requests
import sys
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    user_id = sys.argv[1]
    user = [user for user in data if user.get('id') == int(user_id)][0]
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = response.json()
    tasks = [task for task in data if task.get('userId') == int(user_id)]
    with open("{}.csv".format(user_id), "w") as f:
        [f.write('"{}","{}","{}","{}"\n'.format(
            user_id, user.get('username'), task.get('completed'),
            task.get('title'))) for task in tasks]