#!/usr/bin/python3
""""
Python script that exports data from an API in JSON format.
"""
import requests
import sys
import json

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
    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')} for task in tasks]}, f)
