from flask import render_template, request
from app import app
from models.events_list import events, add_new_event
from models.event import Event

@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)

@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    name_of_event = request.form["name_of_event"]
    no_of_guests = request.form["no_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    is_recurring = bool(request.form["recurring"])
    new_event = Event(event_date, name_of_event, no_of_guests, room_location, description, is_recurring)      
    add_new_event(new_event)
    return render_template("index.html", title="Home", events=events)