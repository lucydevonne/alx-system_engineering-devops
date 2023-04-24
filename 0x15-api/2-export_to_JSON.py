import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    # Get employee information
    employee_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()

    # Get employee todo list
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': employee_id}).json()

    # Filter completed tasks
    completed_tasks = [{'task': task['title'], 'completed': task['completed'], 'username': employee_info['username']} for task in todo_list if task['completed']]

    # Write JSON data to file
    file_name = '{}.json'.format(employee_id)
    with open(file_name, 'w') as file:
        json.dump({employee_id: completed_tasks}, file)

    print('Data exported to {} file.'.format(file_name))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    else:
        print('Usage: python script.py EMPLOYEE_ID')

