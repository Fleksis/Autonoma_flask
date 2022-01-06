from flask import Flask, render_template, request, Response
from settings import app
from models import User
from business_logic import save_car_booking, get_car_booking, save_user_registration

@app.route('/')
def home():
  return render_template("index.html", cars = get_car_booking())

@app.route('/admin')
def admin():
  return render_template("admin.html")

@app.route('/izvele')
def izvele():
  return render_template("Klienta_lapa_izvl.html")

@app.route('/register')
def register():
  return render_template("templates/register.html")

@app.route('/add_car', methods=["POST"])
def add_car():
  if request.method == "POST":
    save_car_booking(request.form)
    return "Dati tika veiksmīgi reģistrēti!"
  else:
    return "404"

@app.route('/new_user_register', methods=['POST'])
def new_user_register():
  if request.method == "POST":
    save_user_registration(request.form)
    return "Done"
  else:
    return "404"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)