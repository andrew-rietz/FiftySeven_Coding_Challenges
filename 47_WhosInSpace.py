"""

Did you now you can find out exactly who's in space
right now? The Open Notify API provides that
information. Visit
http://api.open-notify.org/astros.json to see not
only how many people are currently in space but also
their names and which spacecraft they're on.

Create a program that pulls in this data and
displays the information from thsi API in a
tabular format.

___________________
Example Output
___________________
There are three people in space right now:

Name                | Craft
--------------------|-------
Gennady Padalka     | ISS
Mikhail Kornienko   | ISS
Scott Kelly         | ISS

___________________
Constraints
___________________
- Read the data directly from the API and parse
the results each time the program is run. Don't
download the data as text and read it in.

"""


"""
http://api.open-notify.org/astros.json

Sample API output (JSON):

{
    "message": "success",
    "number": 6,
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "David Saint-Jacques"
        },
        {
            "craft": "ISS",
            "name": "Anne McClain"
        },
        {
            "craft": "ISS",
            "name": "Alexey Ovchinin"
        },
        {
            "craft": "ISS",
            "name": "Nick Hague"
        },
        {
            "craft": "ISS",
            "name": "Christina Koch"
        }
    ]
}
"""


def prettyOut(people):
    longestName = max([len(person["name"]) for person in people]) + 1
    longestCraftName = max([len(person["craft"]) for person in people]) + 1
    longestCraftName = max(longestCraftName, len("Craft "))

    prettyOutput = f"There are {len(people)} people in space right now:\n\n"
    prettyOutput += "Name".ljust(longestName) + "| " + "Craft".ljust(longestCraftName)
    prettyOutput += "\n" + "-" * longestName + "|-" + "-" * longestCraftName

    for person in people:
        prettyOutput += (
            "\n"
            + f"{person['name']}".ljust(longestName)
            + "| "
            + f"{person['craft']}".ljust(longestCraftName)
        )

    return prettyOutput


def main():
    import requests

    apiResponse = requests.get("http://api.open-notify.org/astros.json")
    if apiResponse.status_code != 200:
        # Would raise an error if response code was not 200
        raise ApiError("GET /open-notify/ {}".format(resp.status_code))

    people = apiResponse.json()["people"]

    print(prettyOut(people))


main()
