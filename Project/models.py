from pymongo import MongoClient

# Create a client for MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Connect to the MongoDB server
db = client["timetable"]

# Collections
users = db.users
subjects = db.subjects
rooms = db.rooms
classes = db.classes