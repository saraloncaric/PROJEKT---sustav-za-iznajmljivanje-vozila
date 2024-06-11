import sqlite3
import click 
from flask import current_app, g

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and crate new tables"""
    init_db()
    click.echo('Initialized the database')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def execute_query(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_data(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()

def update_data(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()

def delete_data(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()
