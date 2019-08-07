"""

The data provided by external services can give you a jumping-off
point to create your own application.

Write a program that displays information about a given movie.
Prompt for a search query and display the title, year, rating,
running time, and a synopsis, if one exists. Then, if the audience
score is above 80%, recommend that the user watch this movie right
now. If the score is below 50%, recommend that the user avoid the
movie at all costs.

___________________
Example Output
___________________

Enter the name of a movie: Guardians of the Galaxy

Title: Guardians of the Galaxy
Year: 2014
Rating: PG-13
Running Time: 121 minutes

Description: From Marvel...

You should watch this movie right now!

___________________
Constraints
___________________
Use the Rotten Tomatoes API at http://developer.rottentomatoes.com/
and obtain an API key.

"""

"""
NOTE: It looks like the rottentomatoes api no longer exists.
Using the api available for OMDb http://www.omdbapi.com
"""


class MovieData:
    def __init__(self, query, api_response):
        self.query = query
        self.api_response = api_response
        self.title = self.api_response["Title"]
        self.year = self.api_response["Year"]
        self.rating = self.api_response["Rated"]
        self.run_time = self.api_response["Runtime"]
        self.viewer_ratings = {"Rotten Tomatoes": "", "IMDb": ""}

    def print_details(self):
        details = (
            f"\nTitle: {self.title}\n"
            + f"Year: {self.year}\n"
            + f"Rating: {self.rating}\n"
            + f"Running Time: {self.run_time}\n"
        )

        return details

    def recommended(self):
        viewer_ratings = self.api_response["Ratings"]
        for rating in viewer_ratings:
            if rating["Source"] == "Rotten Tomatoes":
                self.viewer_ratings["Rotten Tomatoes"] = rating["Value"]

        try:
            if float(self.viewer_ratings["Rotten Tomatoes"].replace("%", "")) > 80:
                return (
                    "You should watch this movie right now! "
                    + f"{self.title} has a Rotten Tomatoes rating of "
                    + f'{self.viewer_ratings["Rotten Tomatoes"]}.'
                )
            else:
                return (
                    f"{self.title} has a Rotten Tomatoes rating of "
                    + f'{self.viewer_ratings["Rotten Tomatoes"]}.'
                )
        except ValueError:
            return "No Rotten Tomatoes data for this movie."


def OMDb_api(query, api_key):
    import requests

    api_request = (
        "http://www.omdbapi.com/?" + f"apikey={api_key}&" + f"t={query}&" + "r=json"
    )

    api_response = requests.get(api_request)

    if api_response.status_code != 200:
        return "Sorry, the request failed"
    else:
        return api_response.json()


def main():

    query = input("Enter the name of a movie: ")
    api_key = input("Enter the API key: ")

    api_response = OMDb_api(query, api_key)

    if api_response == "Sorry, the request failed":
        print(api_response)
    elif "Error" in api_response.keys():
        print("Sorry, that movie wasn't found.")
    else:
        movie = MovieData(query, api_response)
        print(movie.print_details())
        print(movie.recommended() + "\n")


main()
