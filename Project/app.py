from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# MongoDB Client
client = MongoClient(app.config["MONGO_URI"])
db = client["timetable"]

# Collections
users = db["users"]
subjects = db["subjects"]
rooms = db["rooms"]
classes = db["classes"]

# Home Route - Show Timetable (index page)
@app.route('/')
def index():
    all_classes = list(classes.find())
    for c in all_classes:
        c["_id"] = str(c["_id"])
        c["subject_id"] = str(c["subject_id"])
        c["teacher_id"] = str(c["teacher_id"])
        c["room_id"] = str(c["room_id"])
    return render_template('index.html', classes=all_classes)

# User Management Route
@app.route('/users')
def users_page():
    all_users = list(users.find())
    for u in all_users:
        u["_id"] = str(u["_id"])
    return render_template('users.html', users=all_users)

# Subject Management Route
@app.route('/subjects')
def subjects_page():
    all_subjects = list(subjects.find())
    for s in all_subjects:
        s["_id"] = str(s["_id"])
    return render_template('subjects.html', subjects=all_subjects)

# Room Management Route
@app.route('/rooms')
def rooms_page():
    all_rooms = list(rooms.find())
    for r in all_rooms:
        r["_id"] = str(r["_id"])
    return render_template('rooms.html', rooms=all_rooms)

# Timetable (Classes) Route
@app.route('/classes')
def classes_page():
    all_classes = list(classes.find())
    for c in all_classes:
        c["_id"] = str(c["_id"])
        c["subject_id"] = str(c["subject_id"])
        c["teacher_id"] = str(c["teacher_id"])
        c["room_id"] = str(c["room_id"])
    return render_template('classes.html', classes=all_classes)

# Run Flask App
if __name__ == '__main__':
    app.run()