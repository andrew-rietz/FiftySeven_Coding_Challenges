## 55 -- Text Sharing
Create a web application that lets users share a snippet of text, similar to
http://pastie.org. The program you write should follow these specifications:

* The user should enter the text into a text area and save the text.  
* The text should be stored in a data store.  
* The program should generate a URL that can be used to retrieve the saved text.  
* When a user follows that URL, the text should be dis-played, along with an invitation to edit the text.  
* When a user clicks the Edit button, the text should be copied and placed in the same interface used to create
new text snippets.  

***
[Additional constraints and challenges available in the full text.](https://www.amazon.com/Exercises-Programmers-Challenges-Develop-Coding/dp/1680501224)

***

## Notes to Self
Additional notes on the creation / setup that will (hopefully) be useful for
reference in the future.

#### Create Virtual Environment
[Link to Python Documentation](https://docs.python.org/3/library/venv.html)
```
pip install virtualenv
python -m venv <</path/to/new/virtual/environment>>
source <</path/to/new/virtual/environment>>/bin/activate
```
To deactivate:   
`deactivate`

#### Set Up PSQL
Create database using superuser account  
`sudo -u <<name_of_user>> createdb <<name_of_database>>`  

Access database  
`psql -U <<name_of_user>> -d <<name_of_database>>`

Or, if superuser name is the same as your username on your computer:  
```
sudo -u <<name_of_user>> createdb <<name_of_database>>
psql <<name_of_database>>
```  

Getting the database URI:
`postgresql://localhost/<<name-of-database>>`
[Stackoverflow](https://stackoverflow.com/questions/3582552/postgresql-connection-url)

#### Set Up and Check Flask Runs
(After you've set up your application or application factory...)
If your flask app is set up as a package:  
```
export FLASK_APP=<<name-of-your-package>>
export FLASK_ENV=development
flask run
```
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/#run-the-application)  

If your flask app is a single file:
```
export FLASK_APP=<<your-file-name.py>>
flask run
```
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)

#### Using psycopg2 For Database Manipulation
For this project, will not be using an ORM (i.e., SQLAlchemy). Instead,
use psycopg2.
```
pip install psycopg2
```


***
## Resources
[Flask Official Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)
[Explore Flask Docs](http://exploreflask.com/en/latest/index.html)
[PSQL and psycopg2 Basics](https://medium.com/@gitaumoses4/python-and-postgresql-without-orm-6e9d7fc9a38e)
[PSQL and psycopg2 Examples](https://hackersandslackers.com/psycopg2-postgres-python-the-old-fashioned-way/)
[Deploying a Flask App](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)
