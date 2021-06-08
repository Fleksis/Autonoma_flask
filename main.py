from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def home():
  return render_template("Klienta_lapa.html")


@app.route('/admin')
def admin():
  return render_template("adminlappa.html")

@app.route('/izvele')
def izvele():
  return render_template("Klienta_lapa_izvl.html")

app.run(host='0.0.0.0', port=8080)