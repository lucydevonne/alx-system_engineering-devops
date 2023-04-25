#!/usr/bin/python3

"""
This Python script retrieves information about a given employee's TODO list progress
using the REST API provided by https://jsonplaceholder.typicode.com.

Usage:
    $ python3 employee_todo.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee to retrieve information for.

Format:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""

import csv
import requests
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
    employee_username = user_info['username']
    employee_id = user_info['id']

    # Get user's to-do list by ID
    todo_url = "{}/todos".format(url_base)
    todo_params = {"userId": employee_id}
    todo_response = requests.get(todo_url, params=todo_params)
    todo_list = todo_response.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Print progress report
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))

    # Write data in CSV
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                     'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo_list:
            writer.writerow({
               'USER_ID': task['userId'],
               'USERNAME': employee_username,
               'TASK_COMPLETED_STATUS' : task['completed'],
               'TASK_TITLE': task['title']
            })

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

