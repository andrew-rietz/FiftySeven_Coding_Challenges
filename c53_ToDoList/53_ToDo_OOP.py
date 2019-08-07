"""

Write a command-line todo list program that meets the following
specifications:

- Prompt the user to enter a chore or task. Store the task in a
permanent location that the the task persists when the program is
restarted.
- Allow the user to enter as many tasks as desired but stop
entering tasks by entering a blank task. Do not store the blank
task.
- Display all the tasks.
- Allow the user to remove a task, to signify it's been completed.

___________________
Constraints
___________________

- Store the data in an external data source
- If you're using a server-side language, consider persisting the
data to Redis
- Consider persisting the database to a third-party service like
Parse or Firebase

"""

import collections
import datetime
import requests
import config
import json

PROJECT_ID = config.fb_PROJECT_ID
API_STRING = f"https://{PROJECT_ID}.firebaseio.com/oop"


class ToDoList:
    def __init__(self):
        self.data = collections.OrderedDict()
        return

    def __str__(self):
        user_display = [
            " " + "#".ljust(5) + "|" + " " + "Date".ljust(12) + "|" + " Task",
            "-" * 40,
        ]
        counter = 0
        for creation_date, task in self.data.items():
            user_display += [f" {str(counter).ljust(5)}| {creation_date[:10].ljust(12)}| {task}"]
            counter += 1
        return "\n".join(user_display)

    def remove_task(self, task_id):
        del self.data[task_id]
        return "Item removed. "

    def add_task(self, task_detail):
        task_id = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %f")
        self.data[task_id] = task_detail
        return "Item added. "

    def fetch(self):
        fetch_data = requests.get(API_STRING + ".json")
        if fetch_data.status_code != 200:
            return "Error fetching data from server. Please try again later."
        elif not fetch_data.json():
            return "No existing data"
        else:
            self.data = fetch_data.json()
            return "Success"

    def post(self):
        payload = json.dumps(self.data)
        post_data = requests.put(API_STRING + ".json", payload)
        if post_data.status_code != 200:
            return "Error fetching data from server. Please try again later."
        else:
            return "Success"


def main():

    todo = ToDoList()
    data_fetched = todo.fetch()
    if "Error" not in data_fetched:
        print("Welcome!")
    else:
        print("Error retrieving data from the server")
        return

    while True:
        user_command = input("Enter a command [show, new, mark complete, exit]: ")

        if user_command.lower().strip() == "exit":
            if todo.post() == "Success":
                print("Session data saved to server.")
            else:
                print("Error ending session. Modifications not saved to server.")
            break
        elif user_command.lower().strip() == "new":
            n_tasks = 0
            print("\n" * 2)
            while True:
                task_detail = input("Enter a task (enter a blank line to exit):\n")
                if task_detail.strip() == "":
                    print(f"{n_tasks} tasks added.")
                    break
                else:
                    print(todo.add_task(task_detail), end = " ")
                    n_tasks += 1
        elif user_command.lower().strip() == "show":
            print("\n" * 2 + str(todo) + "\n" * 2)
        elif user_command.lower().strip() == "mark complete":
            if not todo.data:
                print("You must create a list before you can delete tasks")
                break
            n_tasks = 0
            while True:
                print("\n" * 2 + str(todo) + "\n")
                task_index = input("Enter a task # to delete (or a blank line to exit): ")
                if task_index.strip() == "":
                    print(f"{n_tasks} tasks deleted.")
                    break
                try:
                    task_index = int(task_index)
                except ValueError:
                    print("Invalid task #, please try again.")
                    continue
                if task_index in range(len(todo.data)):
                    task_id, task_detail = list(todo.data.items())[task_index]
                    todo.remove_task(task_id)
                    n_tasks += 1
                    if todo.data == {}:
                        print(f"{n_tasks} tasks deleted. No tasks remaining.")
                        break
                else:
                    print("Invalid task #, please try again.")

        else:
            print("Invalid command, try again.")


main()
