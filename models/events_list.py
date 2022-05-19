from models.event import * 
import datetime 

event1 = Event(datetime.date(2022,8,23), "Jones Wedding", 50, "The Royal Suite", "50 dinner guests", False)
event2 = Event(datetime.date(2022,9,13), "Smith Wedding", 20, "The Charles Suite", "20 dinner guests and disco", False)
event3 = Event(datetime.date(2022,10,10), "70th Birthday Party", 15, "The Royal Suite", "buffet", True)

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
