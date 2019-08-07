"""

Using the OpenWeaterhMap API at
http://openweathermap.org/current, create a program
that prompts for a city name and returns the
current temperature for the city.

___________________
Example Output
___________________

Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit

___________________
Constraints
___________________
Keep the processing of the weather feed separate
from the part of your program that displays the
results.

"""


def getInputs():
    searchCity = input(
        "Where would you like to know the weather? [Enter a city in the United States] "
    )
    apiKey = input("What is the API key? ")
    return (searchCity, apiKey)


def main():
    import requests

    (searchCity, apiKey) = getInputs()
    apiRequest = (
        f"http://api.openweathermap.org/data/2.5/weather"
        + f"?q={searchCity},us"
        + "&units=imperial"
        + f"&APPID={apiKey}"
    )

    apiResponse = requests.get(apiRequest)
    if apiResponse.status_code != 200:
        # Would raise an error if response code was not 200
        raise ApiError("GET /openweather/currentweather/ {}".format(resp.status_code))

    weatherDetails = apiResponse.json()["main"]

    print(
        f"The current temperature in {searchCity} "
        + f"is {weatherDetails['temp']:.0f} degrees Fahrenheit."
    )


main()
