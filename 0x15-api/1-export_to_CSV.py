#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve information about a given employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee to retrieve information for.

    Returns:
        None.

    Raises:
        None.
    """
    url_base = "https://jsonplaceholder.typicode.com"

    # Get user info by ID
    user_url = "{}/users/{}".format(url_base, employee_id)
    user_response = requests.get(user_url)
    user_info = user_response.json()
    employee_name = user_info['name']

    # Get user's to-do list by ID
    todo_url = "{}/todos".format(url_base)
    todo_params = {"userId": employee_id}
    todo_response = requests.get(todo_url, params=todo_params)
    todo_list = todo_response.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Print progress report
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name,
        num_completed_tasks,
        total_tasks
    ))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

    # Write data to CSV file
csv_filename = "employee_{}_todo.csv".format(employee_id)
with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ['userId', 'task', 'completed']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for task in todo_list:
        writer.writerow({
            'userId': task['userId'],
            'task': task['title'],
            'completed': task['completed']
        })



if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
