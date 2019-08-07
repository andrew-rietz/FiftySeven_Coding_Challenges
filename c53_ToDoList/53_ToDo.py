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

import datetime
import requests
import config
import json

PROJECT_ID = config.fb_PROJECT_ID
API_STRING = f"https://{PROJECT_ID}.firebaseio.com/rest"


def new():

    n_items = 0
    while True:
        todo_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %f")
        todo_msg = input("Add an item to your todo list (enter a blank line to exit): ")

        if todo_msg.lower().strip() == "":
            return f"{n_items} items added to todo list."

        api_request = requests.get(API_STRING + "/todo.json")
        if api_request.status_code != 200:
            return "Error adding data from API. Check database credentials."
        else:
            request_json = api_request.json()
            payload = {todo_date: todo_msg}
            if request_json:
                delivery = requests.patch(
                    API_STRING + f"/todo.json", data=json.dumps(payload)
                )
            else:
                delivery = requests.put(
                    API_STRING + f"/todo.json", data=json.dumps(payload)
                )

            if delivery.status_code != 200:
                print("Error adding Item")
            else:
                n_items += 1
                print("Item added.", end=" ")


def show():
    delivery = requests.get(API_STRING + "/todo.json")
    if delivery.status_code != 200:
        return "Error retrieving todo list"
    else:
        json_response = delivery.json()
        if json_response:
            todo_msgs = ["\n", " Date".ljust(11) + " | To Do", "-" * 60]
            for date__time in json_response.keys():
                date = date__time[:10]
                todo_msgs += [f" {date.ljust(10)}" + " | " + json_response[date__time]]
        else:
            return "Sorry, you must create a todo list first."

        return "\n".join(todo_msgs) + "\n"


def delete():
    api_request = requests.get(API_STRING + "/todo.json")
    if api_request.status_code != 200:
        return "Error getting data from API"

    request_json = api_request.json()

    if not request_json:
        return "Sorry, you must create a todo list first."
    # try:
    #     datetime_keys = list(request_json.keys())
    # except AttributeError:

    index__datetime_key = {
        (i + 1): datetime_keys[i] for i in range(0, len(datetime_keys))
    }

    n_items = 0
    while True:
        user_display = [
            (
                str(dict_key).ljust(6)
                + "| "
                + index__datetime_key[dict_key][:10]
                + " | "
                + request_json[index__datetime_key[dict_key]]
            )
            for dict_key in index__datetime_key.keys()
        ]

        del_index = input(
            "\n" * 2
            + ("Index | " + "Date".ljust(10) + " | Item")
            + ("\n" + "-" * 40 + "\n")
            + "\n".join(user_display)
            + "\n" * 2
            + "Enter the index of the item to delete (or enter a blank line to exit): "
        )
        if del_index.strip().lower() == "":
            return f"{n_items} items deleted"

        try:
            del_index = int(del_index)
        except ValueError:
            print("Please enter a valid index (or enter a blank line to exit)")
            continue

        if (del_index) not in index__datetime_key.keys():
            print("Please enter a valid index (or enter a blank line to exit)")
            continue
        else:
            deletion = requests.delete(
                f"https://{PROJECT_ID}.firebaseio.com/rest/todo/{index__datetime_key[del_index]}.json"
            )
            if deletion.status_code != 200:
                return f"Issue deleting record {del_index}. {n_items} items deleted."
            else:
                n_items += 1
                del index__datetime_key[del_index]
                if not index__datetime_key:
                    return f"{n_items} items deleted. No more items on your list."
                else:
                    print("Item deleted")


def main():

    while True:
        user_command = input("Enter a command [show, new, mark complete, exit]: ")

        if user_command.lower().strip() == "exit":
            break
        elif user_command.lower().strip() == "new":
            print(new() + "\n")
        elif user_command.lower().strip() == "show":
            print(show() + "\n")
        elif user_command.lower().strip() == "mark complete":
            print(delete() + "\n")
        else:
            print("Invalid command, try again.")


main()
