"""

Programming languages can create files and folders
too.

Create a program that generates a website skeleton
with the following specifications:

- Prompt for the name of the site
- Prompt for the author of the site
- Ask if the user wants a folder for Javascript
files
- Ask if the user wants a folder for CSS files
- Generate an index.html file that contains the
name of the site inside the <title> tag and the
author in a <meta> tag

___________________
Example Output
___________________
Site name: awesomeco
Author: Max Power
Do you want a folder for JavaScript? y
Do you want a folder for CSS? y
Created ./awesomeco
Created ./awesomeco/index.html
Created ./awesomeco/js/
Created ./awesomeco/css/

"""

"""
Additional details:
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
"""


def getInputs():
    siteName = input("Please enter a name for your site: ")
    author = input("Who is the site's author? ")
    while True:
        includeJSdir = input("Do you want a folder for JavaScript? [Y/N] ")
        if includeJSdir.upper() == "Y" or includeJSdir.upper() == "N":
            includeJSdir = includeJSdir.upper()
            break
    while True:
        includeCSSdir = input("Do you want a folder for CSS? [Y/N] ")
        if includeCSSdir.upper() == "Y" or includeCSSdir.upper() == "N":
            includeCSSdir = includeCSSdir.upper()
            break

    return (siteName, author, includeJSdir, includeCSSdir)


def createDirs(dirs, fileLoc):
    import pathlib

    for dir in dirs:
        try:
            pathlib.Path(f"./{fileLoc}/{dir}").mkdir(exist_ok=True)
            print(f"Created ./{fileLoc}/{dir}")
        except ValueError:
            print(f"Could not create ./{fileLoc}/{dir}")
    return "Directories created"


def createHTMLtext(siteName, author):
    html = f"""
    <title>Site Name: {siteName}</title>
    <meta>Author: {author}</meta>
    """
    return html


def main():
    import os

    (siteName, author, includeJSdir, includeCSSdir) = getInputs()

    dirs = [f"{siteName}"]
    if includeJSdir == "Y":
        dirs.append(f"{siteName}/js")
    if includeCSSdir == "Y":
        dirs.append(f"{siteName}/css")
    fileLoc = os.path.dirname(__file__)
    checkDirsCreated = createDirs(dirs, fileLoc)

    html = createHTMLtext(siteName, author)
    with open(f"./{fileLoc}/{siteName}/index.html", "w") as writer:
        writer.write(html)
        print(f"Created ./{os.path.relpath(writer.name)}")


main()
