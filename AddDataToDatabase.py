import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-361f4-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    "201036":
        {
            "Name": "Salman Khan",
            "Profession": "Actor",
            "Date_of_birth": "27 Dec 1965",
            "Total_attendance": 6,
            "Standing": "Good",
            "year": 35,
            "last_attendance_time": "2023-08-29 00:54:34"
        },
    "201037":
        {
            "Name": "Shah Rukh Khan",
            "Profession": "Actor",
            "Date_of_birth": "2 Nov 1965",
            "Total_attendance": 12,
            "Standing": "Excellent",
            "year": 35,
            "last_attendance_time": "2023-08-29 00:54:34"
        },
    "201038":
        {
            "Name": "Farhan Ansari",
            "Profession": "Student",
            "Date_of_birth": "26 May 2002",
            "Total_attendance": 6,
            "Standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-08-29 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)