from flask import Response, Flask, render_template, request, redirect, session
from flask.helpers import url_for, flash
from settings import app
from models import Car
from business_logic import *
from datetime import date
from flask import jsonify
import json

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

@app.route('/admin/rental_point_manager')
def rental_point():
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin_templates/rental_point.html", rental_points = get_all_rental_points())
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
      return render_template("templates/profile.html", cars = get_cars(), user = get_user_data(session['user']), date = date.today().strftime("%Y-%m-%d"), rental_points = get_all_rental_points())
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route('/add_car_reservantion', methods=["POST"])
def add_car_reservantion():
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

@app.route("/admin/set_rental_point", methods=["POST"])
def set_rental_point():
  try:
    if is_user_logged() and is_user_admin(session['user']):
      set_new_rental_point(request.form)
      flash("Tika pievienots autonomas punkts", "success")
      return redirect(url_for('rental_point'))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/add_car", methods=["POST"])
def add_car():
  try:
    if is_user_logged() and is_user_admin(session['user']):
      set_new_car(request.form)
      flash("Tika pievienota automašīna", "success")
      return redirect(url_for('rental_point'))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))


@app.route("/admin/rental_point/<id>")
def rental_point_detail(id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin_templates/rental_point_detail.html", cars=get_rental_point_cars(id))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/rental_point/delete/<id>")
def rental_point_delete(id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      delete_rental_point(id)
      flash("Tika veiksmīgi izdzēsts autonomas punkts", "success")
      return redirect(url_for('rental_point'))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/rental_point_edit/<id>")
def rental_point_edit_page(id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin_templates/rental_point_edit.html", rental_point=get_rental_point(id))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))


@app.route("/admin/rental_point/edit/<id>", methods=["POST"])
def rental_point_edit(id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      edit_rental_point(id, request.form)
      return redirect(url_for('rental_point'))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/rental_point_detail_edit/<id>")
def rental_point_detail_edit_page(id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      return render_template("admin_templates/rental_point_detail_edit.html", car=get_rental_point_car(id))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/rental_point_detail/edit/<rental_point_id>/<id>", methods=["POST"])
def rental_point_detail_edit(rental_point_id, id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      edit_rental_point_detail(id, request.form)
      return redirect(url_for('rental_point_detail', id=rental_point_id))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))

@app.route("/admin/rental_point_car/delete/<rental_point_id>/<car_id>")
def rental_point_car_delete(rental_point_id, car_id):
  try:
    if is_user_logged() and is_user_admin(session['user']):
      delete_rental_point_car(car_id)
      flash("Tika veiksmīgi izdzēsts autonomas punkts", "success")
      return redirect(url_for('rental_point_detail', id=rental_point_id))
    else:
      return redirect(url_for('home'))
  except Exception as e:
    flash(str(e))
    return redirect(url_for('home'))


# REST API
@app.route("/rental_point_cars/<id>")
def api_rental_point_cars(id):
  cars = []
  for car in get_rental_point_cars(id):
    cars.append(car.serialize())
  return Response(json.dumps(cars), mimetype='application/json')

@app.route("/cars")
def api_get_cars():
  cars = []
  for car in get_cars():
    cars.append(car.serialize())
  return Response(json.dumps(cars), mimetype='application/json')

@app.route("/rental_point/<id>")
def api_rental_point(id):
  return Response(json.dumps(get_rental_point(id).serialize()), mimetype='application/json')

@app.route("/rental_points")
def api_rental_points():
  retal_points = []
  for retal_point in get_all_rental_points():
    retal_points.append(retal_point.serialize())
  return Response(json.dumps(retal_points), mimetype='application/json')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)