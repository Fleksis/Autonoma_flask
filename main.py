from flask import Flask, render_template, request, redirect, session
from flask.helpers import url_for, flash
from settings import app
from models import Car
from business_logic import set_status_code, is_user_logged, save_car_booking, get_user_car_booking, save_user_registration, compare_user_login, get_user_data, get_all_users_cars, is_user_admin, remove_car
from datetime import date

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/admin')
def admin():
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin.html", user_cars = get_all_users_cars())
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route('/admin/car_manager')
def car_manager():
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin_templates/car_manager.html", user_cars = get_all_users_cars())
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route('/about_us')
def izvele():
  return render_template("templates/about_us.html")

@app.route('/register')
def register():
  return render_template("templates/register.html")

@app.route('/login')
def login():
  return render_template("templates/login.html")

@app.route('/profile')
def profile():
  try:
    if is_user_logged():
      return render_template("templates/profile.html", cars = get_user_car_booking(session['user']), user = get_user_data(session['user']), date = date.today().strftime("%Y-%m-%d"))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route('/add_car', methods=["POST"])
def add_car():
  if request.method == "POST":
    save_car_booking(request.form, session['user'])
    return redirect(url_for('profile'))
  else:
    return "404"

@app.route('/delete_car/<id>')
def delete_car(id):
  try:
    remove_car(id)
  except Exception as e:
    flash(str(e))
  if is_user_admin(session['user']):
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('profile'))

@app.route('/new_user_register', methods=['POST'])
def new_user_register():
  try:
    if request.method == "POST":
      save_user_registration(request.form)
      return redirect(url_for('profile'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('register'))

@app.route('/user_login', methods=['POST'])
def user_login():
  try:
    if request.method == "POST":
      compare_user_login(request.form)
      return redirect(url_for('profile'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session['user'] = None
  flash("Jūs veiksmīgi izrakstījāties!")
  return redirect(url_for('home'))

# To:do
@app.route('/admin/set_booking_status/<car_id>/<status_code>')
def set_booking_status(car_id, status_code):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      set_status_code(car_id, status_code)
      return redirect(url_for('admin'))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)