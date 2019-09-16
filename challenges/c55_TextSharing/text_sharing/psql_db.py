import psycopg2
import psycopg2.extras
from psycopg2 import sql
import os
import sys
import click
import json

from flask import current_app, g
from flask.cli import with_appcontext


package_dir = os.path.dirname(os.path.abspath(__file__))

class PSQLDatabase():
    """PSQL Database Connection Class"""

    def __init__(self):
        self.dbname = current_app.config["DB_NAME"]
        self.user = current_app.config["DB_USER"]
        self.host = current_app.config["DB_HOST"]
        self.port = current_app.config["DB_PORT"]
        self.password = current_app.config["DB_USER_PW"]
        self.conn = None

    def load_schema(self):
        """Load the schema.sql file into PSQL using psycopg2"""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                schema_file = os.path.join(package_dir, "schema.sql")
                with open(schema_file, "r") as sql_schema:
                    input_line = sql_schema.read()
                    cur.execute(input_line)
            self.conn.commit()
        except psycopg2.DatabaseError as e:
            print(e)

    def clear_schema(self):
        """Clears the database schema"""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                try:
                    cur.execute(
                        "SELECT table_schema,table_name FROM information_schema.tables " +
                        "WHERE table_schema = 'public' ORDER BY table_schema,table_name"
                    )
                    rows = cur.fetchall()
                    for row in rows:
                        print(f"dropping table: {row[1]}")
                        cur.execute(
                            sql.SQL("drop table {} cascade").format(sql.Identifier(row[1]))
                        )
                    cur.close()
                except:
                    print(f"Error: {sys.exc_info()[1]}")
            self.conn.commit()
            self.conn.close()
        except psycopg2.DatabaseError as e:
            print(e)

    def open_connection(self):
        """Connect to a PSQL Database"""
        try:
            if self.conn is None:
                self.conn = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    host=self.host,
                    port=self.port,
                    password=self.password
                )
            if self.conn.closed:
                self.conn = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    host=self.host,
                    port=self.port,
                    password=self.password
                )
        except psycopg2.DatabaseError as e:
            print(e)
            sys.exit()
        finally:
            print("Connection opened successfully")

    def close_connection(self):
        """Closes connection to a PSQL Database"""
        if self.conn:
            try:
                self.conn.close()
            except psycopg2.DatabaseError as e:
                print(e)
            finally:
                print("Database connection closed.")
        print("No database connection to close.")

    def run_query(self, query, user_inputs=None):
        """Runs a SQL query"""
        try:
            self.open_connection()
            # RealDictCursor allows us to query the returned row(s) by column name
            with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                if "SELECT" in query:
                    records = []
                    cur.execute(query, user_inputs)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()

                    if not records:
                        return None
                    return records

                result = cur.execute(query, user_inputs)
                self.conn.commit()
                affected = f"{cur.rowcount} rows affected."
                cur.close()
                return affected
        except psycopg2.DatabaseError as e:
            print(e)

def get_db():
    """Check if a database object exists, then return or create the database object"""
    if "db" not in g:
        g.db = PSQLDatabase()

    return g.db

def close_db(e=None):
    """Close the database connection"""
    db = g.pop("db", None)

    if db is not None:
        db.close_connection()

# click.command() defines a command line command called 'init-db'
# that calls the init_function and returns a success message
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db = get_db()
    db.load_schema()
    click.echo("Initialized the database.")

def init_app(app):
    """Registers functions with the application"""
    # app.teardown_appcontext() tells flask to call that function
    # when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    # app.cli.add_command() adds a new command that can be called
    # with the `flask` command
    app.cli.add_command(init_db_command)
