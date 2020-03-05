from flask import Flask, render_template, request
import requests
import json
from data import teachers, goals
import random
import pprint
app = Flask(__name__)
with open('teachers.json', "w") as file_write:
    json.dump(teachers, file_write)
with open("teachers.json", "r") as f:
    teachers = json.load(f)

@app.route('/')
def main():
    random_teacher = []
    for i in range(6):
        a = random.randint(1, 11)
        random_teacher.append(a)
    pprint.pprint(teachers)
    return render_template('index.html',teacher = teachers, random = random_teacher)


@app.route('/goals/<goal>/')
def render_goals(goal):
    return render_template('goal.html')

@app.route('/all_profiles/')
def render_all_profile():
    return render_template('all_profile.html',teacher = teachers)


@app.route('/profiles/<id>/')
def render_profile(id):
    return render_template('profile.html', teacher=teachers, id=int(id), goal=goals)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    return render_template('request_done.html')


@app.route('/booking/<id>/<day>/<time>/')
def rander_booking(id, day, time):
    return render_template('booking.htm')


@app.route('/booking_done/')
def rander_booking_done():
    return render_template('booking_done.html')


app.run()
