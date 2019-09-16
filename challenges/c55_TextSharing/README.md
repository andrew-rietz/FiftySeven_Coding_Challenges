## 55 -- Text Sharing
Create a web application that lets users share a snippet of text, similar to
http://pastie.org. The program you write should follow these specifications:

- The user should enter the text into a text area and save the text.  
- The text should be stored in a data store.  
- The program should generate a URL that can be used to retrieve the saved text.  
- When a user follows that URL, the text should be displayed, along with an invitation to edit the text.  
- When a user clicks the Edit button, the text should be copied and placed in the same interface used to create
new text snippets.  

***
## Narrative
The back end of this web application is implemented using Python and Flask with a minimalist front end.
Most styling (CSS) and page layouts (HTML) are borrowed from the
[Flask Official Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).

## Design Decisions
- **Database:** `PostgreSQL`. Seems to be the trendy SQL database of choice these days and many of my other
recent project have features no-sql solutions.
- **Database ORM (or lack thereof):** After some searching around, it appears that SQLAlchemy is the ORM
of choice for SQL database solutions. While this is probably the right approach for a fully-fledged
application, I've opted to use `psycopg2`. Based on my research, SQLAlchemy provides an additional
layer of abstraction between the developer and the database. I hope to gain a better understanding
of database interactions by option for psycopg2 over SQLAlchemy.
- **Flask application:** I've opted for consistency with the simple flask app tutorial which implements
an application factory and makes use of blueprints to organize views and other related code.
[Flask Official Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)
- **HTML and CSS:** I've opted not to do my own custom styling for these elements. This web site
was similar to the site I built following the tutorial provided in the flask documentation
([Flask Official Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)), so I opted to
re-use much of the HTML and CSS from that project with a few tweaks / updates.

I could have opted to pull in some better styling (from [Bootstrap](https://getbootstrap.com/) for example),
but the focus of these challenges is to develop my Python skills.

***
***
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

To connect to PSQL database:
```
self.conn = psycopg2.connect(
              dbname=current_app.config["DB_NAME"],
              user=current_app.config["DB_USER"],
              host=current_app.config["DB_HOST"],
              port=current_app.config["DB_PORT"],
              password=current_app.config["DB_USER_PW"]
          )
```

To query against the database:
1. Open a connection
2. Create a cursor. For this project, we'll specify a `RealDictCursor` which
allows us to query the returned rows by column name
3. Once done with the query, close the cursor

***
## Resources
[Flask Official Docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)
[Explore Flask Docs](http://exploreflask.com/en/latest/index.html)
[PSQL and psycopg2 Basics](https://medium.com/@gitaumoses4/python-and-postgresql-without-orm-6e9d7fc9a38e)
[PSQL and psycopg2 Examples](https://hackersandslackers.com/psycopg2-postgres-python-the-old-fashioned-way/)
[Deploying a Flask App](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)

***

Testing resources:
https://damyanon.net/post/flask-series-testing/
http://www.axelcdv.com/python/flask/postgresql/2018/03/30/flask-postgres-tests.html
https://gist.github.com/amaudy/82cb024e9cf75c202e2b
https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
