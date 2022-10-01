from tabla_html import app
from flask import render_template


@app.route('/')
def render_lists():
    users_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi', 'age' : 35,'email' : 'michaelchoi@codingdojo.com',},
    {'first_name' : 'John', 'last_name' : 'Supsupin', 'age' : 30,'email' : 'john@codingdojo.com',},
    {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age' : 25,'email' : 'mark@codingdojo.com',},
    {'first_name' : 'KB', 'last_name' : 'Tonel', 'age' : 27, 'email' : 'michaelchoi@codingdojo.com',}
    ]

    return render_template("lists.html", users=users_info)