from flask import render_template

from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/cleaning')
def cleaning():
    return render_template('cleaning.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/deals')
def deals():
    return render_template('deals.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/employee')
def employee():
    return render_template('employee.html')
