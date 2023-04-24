import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com"
    employee_response = requests.get(url + "/users/" + str(employee_id))
    employee_name = employee_response.json()["name"]

    todo_response = requests.get(url + "/todos", params={"userId": employee_id})
    todos = todo_response.json()
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo["completed"])

    csv_filename = str(employee_id) + ".csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t{}".format(todo["title"]))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

