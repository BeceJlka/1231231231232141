from flask import Flask, render_template, request
import json
from data import teachers, goals, days
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
    return render_template('index.html',teacher = teachers, random = random_teacher)


@app.route('/goals/<goal>/')
def render_goals(goal):
    teachers_fit_for_goal = []
    for teacher in teachers:
        if goal in teacher['goals']:
            teachers_fit_for_goal.append(teacher)
    print(teachers_fit_for_goal)
    return render_template('goal.html', goal=goal, goals=goals, teachers_fit_for_goal=teachers_fit_for_goal, id=id)

@app.route('/all_profiles/')
def render_all_profile():
    return render_template('all_profile.html',teacher = teachers)


@app.route('/profiles/<int:id>/')
def render_profile(id):
    return render_template('profile.html', teacher=teachers, goals=goals, id=id, days = days)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/', methods=["POST"])
def render_request_done():
    name = request.form.get("clientName")
    phone = request.form.get("clientPhone")
    goal = request.form.get("goal")
    time = request.form.get("time")
    requests = {"name": request.form.get("clientName"),
                "phone": request.form.get("clientPhone"),
                "goal":request.form.get("goal"),
                "time":request.form.get("time")}
    with open('request.json', "w") as f_write:
        json.dump(requests,f_write)
    return render_template('request_done.html', goal=goal, time=time, name=name, phone=phone, goals = goals)


@app.route('/booking/<int:id>/<day>/<time>/')
def rander_booking(id, day, time):
    return render_template('booking.html', teacher=teachers, id=id, day=day, time=time, days = days)


@app.route('/booking_done/', methods=["POST"])
def rander_booking_done():
    cteacher = request.form.get("clientTeacher")
    day = request.form.get("clientWeekday")
    time = request.form.get("clientTime")
    username = request.form.get("clientName")
    phone = request.form.get("clientPhone")
    booking = {'clientTeacher': request.form['clientTeacher'],
               'clientWeekday': request.form['clientWeekday'],
               'clientTime': request.form['clientTime'],
               'clientName': request.form['clientName'],
               'clientPhone': request.form['clientPhone']}
    with open('booking.json', "w") as f_write:
        json.dump(booking,f_write)
    return render_template('booking_done.html', username=username, phone=phone, day=day, time=time, days=days,
                           teacher=teachers, id=int(cteacher))


app.run()
