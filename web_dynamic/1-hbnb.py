#!/usr/bin/python3
""" Start a Flask Web Application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/1-hbnb')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('1-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)