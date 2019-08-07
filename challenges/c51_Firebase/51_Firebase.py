"""

Some external services allow you to update data, not just read it.
Firebase is a service that lets you create your own database so you
can save data for web, mobile, and desktop applications. And you can
use it with any programming language, thanks to its JSON-based API.

Create a simple command-line application that lets you save and
show notes using Firebase to save the notes. The application should
support the following commands:

"mynotes new" >>> Add a note to the database
"mynotes show" >>> display all existing notes

___________________
Example Output
___________________

$ mynotes new Learn how to invert binary trees
Your note was saved.

$ mynotes show
2050-12-31 - Learn how to invert binary trees
2050-12-30 - Notetaking on the command line is cool.

___________________
Constraints
___________________
- Create a configuration file that stores the API key
- Use the REST documentation at https://www.firebase.com/docs/rest
instead of a premade client library.

"""

import datetime
import requests
import config
import json

PROJECT_ID = config.fb_PROJECT_ID
API_STRING = f"https://{PROJECT_ID}.firebaseio.com/rest"

# Commands
# new
def new():

    note_date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_note = note_date + " | " + input("Enter a note: ")

    # check whether the key (note_date) already exists, if yes, get count of notes
    api_request = requests.get(API_STRING + "/notes.json")
    if api_request.status_code != 200:
        return "Error getting data from API"
    else:
        request_json = api_request.json()
        try:
            date_keys = list(request_json.keys())
            notes = {k: request_json[k] for k in request_json.keys()}
        except AttributeError:
            # No keys exist at this point
            date_keys = None

        if request_json and note_date in date_keys:
            note_id = int(list(notes[note_date].keys())[-1][1:]) + 1
            note_id = "n" + str(note_id)
        else:
            note_id = "n0"

        payload = {note_id: new_note}

    if note_id == "n0":
        delivery = requests.put(
            API_STRING + f"/notes/{note_date}.json", data=json.dumps(payload)
        )
    else:
        delivery = requests.patch(
            API_STRING + f"/notes/{note_date}.json", data=json.dumps(payload)
        )

    if delivery.status_code != 200:
        return "Error adding note"
    else:
        return "Note added"


# show
def show():
    delivery = requests.get(API_STRING + "/notes.json")
    if delivery.status_code != 200:
        return "Error retrieving notes"
    else:
        json_response = delivery.json()
        try:
            note_dates = json_response.keys()
        except AttributeError:
            return "Sorry, you must enter notes first"

        key_notes = ["\n", "Date".ljust(10) + " | Note", "-" * 60]
        for json_key in json_response.keys():
            key_notes += json_response[json_key].values()

        return "\n".join(key_notes) + "\n"


# delete
def delete():
    api_request = requests.get(API_STRING + "/notes.json")
    if api_request.status_code != 200:
        return "Error getting data from API"
    else:
        request_json = api_request.json()

        try:
            date_keys = list(request_json.keys())
        except AttributeError:
            return "Sorry, you must enter notes first"

        date_key__note_id__note__index = []
        disp_index = 0
        for date_key in date_keys:
            note_ids = request_json[date_key].keys()
            for note_id in note_ids:
                date_key__note_id__note__index.append(
                    [date_key, note_id, request_json[date_key][note_id], disp_index]
                )
                disp_index += 1

        user_display = ["Index | " + "Note Date".ljust(10) + " | Note"]
        user_display += ["-" * 40]
        for item in date_key__note_id__note__index:
            user_display += [str(item[3]).ljust(6) + "| " + item[2]]

        while True:
            try:
                del_index = input(
                    "\n"
                    + "\n".join(user_display)
                    + "\n" * 2
                    + "Enter the index of the note to delete (or cancel): "
                )
                if del_index.strip().lower() == "cancel":
                    return "No items deleted"
                else:
                    del_index = int(del_index)
                    break
            except ValueError:
                print("Please enter a valid index or the word 'exit'")

        item = date_key__note_id__note__index[del_index]
        del_api_call = (
            f"https://{PROJECT_ID}.firebaseio.com/rest/notes/{item[0]}/{item[1]}.json"
        )
        deletion = requests.delete(del_api_call)
        if deletion.status_code != 200:
            print(deletion.json())
            return "Issue deleting record"
        else:
            return "Item deleted"


def main():

    while True:
        user_command = input("Enter a command [show, new, delete, exit]: ")

        if user_command.lower().strip() == "exit":
            break
        elif user_command.lower().strip() == "new":
            print(new())
        elif user_command.lower().strip() == "show":
            print(show())
        elif user_command.lower().strip() == "delete":
            print(delete())
        else:
            print("Invalid command, try again.")


main()
