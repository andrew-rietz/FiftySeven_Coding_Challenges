source ./env_trivia/bin/activate
source .env
export FLASK_APP=trivia_app
export FLASK_ENV=development
# Only need to init the DB once -- then migrations
# and upgrades should handle DB modifications
# flask db init
flask db migrate
flask db upgrade
flask run
