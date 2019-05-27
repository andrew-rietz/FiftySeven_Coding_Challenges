"""

Some services provide search features and give you a lot of control
over the results you get back. All you have to do is construct
the right kind of request.

Create a program with a graphical interface that takes in a search
string and displays photographs that match that search string. Use
Flickr's public photo feed as your service.

(https://www.flickr.com/services/feeds/docs/photos_public/)

___________________
Example Output
___________________

Your program should display the photographs like this:

Photos about "<<search term>>"
---------   ---------   ---------
|       |   |       |   |       |
|       |   |       |   |       |
|       |   |       |   |       |
|       |   |       |   |       |
---------   ---------   ---------
___________________
Constraints
___________________
Because this is a graphical program, you'll need to display the
pictures from the API. If you're using Javascript, do this with
HTML and the DOM. Don't use jQuery or any external frameworks. If
you're using Java, try building a desktop application with Swing
or an Android application. If you're using a language with a rich GUI
toolkit, create an HTML page and open it with the local browser.

"""

def getInputs():
    searchTerm = input(
        "What kind of pictures would you like? "
    )
    return (searchTerm)

def writeHTML(searchTerm, pictures):
    import math

    pageHTML =(
    """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Flickr Photos</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
          .img-thumbnail{
            height: 200px;
            width: 200px;
            object-fit: cover;
          }
        </style>
      </head>
      <body>
        <div class="container">
"""
    )
    pageHTML += f'\
            <h2>Photos about "{searchTerm}"</h2>'
    pageHTML += ('''
                <div class="row">'''
                )
    for picture in pictures:
            pageHTML += (
            f"""
            <div class="px-0">
              <img src="{picture}" alt="Picture Not Found" class="img-thumbnail">
            </div>
            """
            )

    pageHTML += "</div>"

    pageHTML += (
    """
          </div>
      </body>
    </html>
    """
    )

    with open("./49_FlickrPhotos/49_html.html", "w") as writer:
        writer.write(pageHTML)

    return "File created"

def main():
    import requests
    import json

    (searchTerm) = getInputs()
    apiRequest = (
        f"https://api.flickr.com/services/feeds/photos_public.gne?"
        + f"tags={searchTerm}&format=json"
    )

    apiResponse = requests.get(apiRequest)
    jsonResponse = json.loads(apiResponse.text[15:len(apiResponse.text)-1])
    imgLinks = [dict["media"]["m"] for dict in jsonResponse["items"]]

    print(writeHTML(searchTerm, imgLinks))

main()
