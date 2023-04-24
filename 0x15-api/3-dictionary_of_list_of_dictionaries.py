#!/usr/bin/python3

import json
import requests
import sys

def get_employee_tasks(employee_id):
    url_base = "https://jsonplaceholder.typicode.com"

    # get user info by id
    user_response = requests.get(f"{url_base}/users/{employee_id}")
    user_info = user_response.json()
    username = user_info['username']

    # get user's to-do list by id
    todo_response = requests.get(f"{url_base}/todos", params={"userId": employee_id})
    todo_list = todo_response.json()

    # create list of tasks
    tasks = []
    for task in todo_list:
        task_dict = {
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        }
        tasks.append(task_dict)

    return tasks

def export_all_tasks():
    url_base = "https://jsonplaceholder.typicode.com"

    # get all user ids
    users_response = requests.get(f"{url_base}/users")
    users = users_response.json()

    # create dictionary of tasks for each user
    tasks_by_user = {}
    for user in users:
        user_id = user['id']
        tasks = get_employee_tasks(user_id)
        tasks_by_user[user_id] = tasks

    # write dictionary to JSON file
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(tasks_by_user, outfile)

if __name__ == "__main__":
    export_all_tasks()

