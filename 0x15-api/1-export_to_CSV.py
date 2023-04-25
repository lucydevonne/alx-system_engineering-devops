#!/usr/bin/python3

"""
A script that uses the JSONPlaceholder API to retrieve information about a given employee's
TODO list progress and save it to a CSV file.
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
    url = "https://jsonplaceholder.typicode.com"

    # Retrieve employee information by ID
    employee_response = requests.get("{}/users/{}".format(url, employee_id))
    employee_name = employee_response.json()["name"]

    # Retrieve employee's TODO list by ID
    todo_response = requests.get("{}/todos".format(url), params={"userId": employee_id})
    todos = todo_response.json()
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo["completed"])

    # Save employee TODO list to CSV file
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

    # Print progress report
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t{}".format(todo["title"]))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
