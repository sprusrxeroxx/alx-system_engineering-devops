#!/usr/bin/python3
""""
Python script that exports all employee task data
from an API in JSON format.
"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    tasks = response.json()
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []
        for task in tasks:
            if task['userId'] == user_id:
                user_tasks.append({
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': username
                })
        data[user_id] = user_tasks
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
