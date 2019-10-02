## 57 -- Trivia App
Create a multiple-choice trivia application.
  * Read questions, answers, and distractors (wrong answers) from a file.
  * When a player starts a game
    * Choose questions at random.
    * Display the answer and distractors in a random order.
    * Track the number of correct answers.
    * End the game when the player selects a wrong answer.

***
## Narrative
A simple trivia web application.

## Design Decisions
* Use of a flask application that makes use of the application factory design pattern
* Using sqlalchemy with a psql database


## .env file
Hosts privileged information about our app  
Variables set to the environment using:  
`export SOME_VAR_NAME=value`  
Must source env file or utilize a helper package like dotenv. In this case,
we'll source the package from our shell script `start.sh`


## Database Setup
* install Flask-SQLAlchemy
* install Flask-Migrate
* Add database to application factory
* Define database models (`models.py`)
* Initiliaze and perform first migration for the database:
  * flask db init (sets up the `migrations` directory)
  * flask db migrate -m "<<some description of migration>>" (generates a migration script)
  * flask db upgrade (applies changes to the database)



## References
https://hackersandslackers.com/demystifying-flask-application-factory
https://hackingandslacking.com/demystifying-flasks-application-context-c7bd31a53817

Shell scripting: https://stackoverflow.com/questions/40894631/how-does-one-enter-a-python-virtualenv-when-executing-a-bashscript
