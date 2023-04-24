#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    url_base = "https://jsonplaceholder.typicode.com"
    
    # get user info by id
    user_response = requests.get(f"{url_base}/users/{employee_id}")
    user_info = user_response.json()
    employee_name = user_info['name']
    
    # get user's to-do list by id
    todo_response = requests.get(f"{url_base}/todos", params={"userId": employee_id})
    todo_list = todo_response.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)
    
    # print progress report
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

