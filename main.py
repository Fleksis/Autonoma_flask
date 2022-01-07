from flask import Flask, render_template, request, redirect
from flask.helpers import url_for, flash
from settings import app
from models import User
from business_logic import save_car_booking, get_car_booking, save_user_registration

@app.route('/')
def home():
  return render_template("index.html", cars = get_car_booking())

@app.route('/admin')
def admin():
  return render_template("admin.html")

@app.route('/about_us')
def izvele():
  return render_template("templates/about_us.html")

@app.route('/register')
def register():
  return render_template("templates/register.html")

@app.route('/login')
def login():
  return render_template("templates/login.html")

@app.route('/add_car', methods=["POST"])
def add_car():
  if request.method == "POST":
    save_car_booking(request.form)
    return "Dati tika veiksmīgi reģistrēti!"
  else:
    return "404"

@app.route('/new_user_register', methods=['POST'])
def new_user_register():
  try:
    if request.method == "POST":
      save_user_registration(request.form)
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('register'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)