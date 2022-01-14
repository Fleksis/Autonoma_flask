from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

_metadata = MetaData(naming_convention=convention)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AutoNomasDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, metadata=_metadata)

# Migrate
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(5), nullable=False)
    car = db.relationship("UserCar", cascade="all, delete")

    def __repr__(self):
        return '<User %r>' % (self.firstname)

class UserCar(db.Model):
    __tablename__ = 'user_car'
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(20), nullable=False)
    from_date = db.Column(db.String(20), nullable=False)
    to_date = db.Column(db.String(20), nullable=False)
    booked_status = db.Column(db.Integer, default=0)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<BookedCars %r %r>' % (self.car , self.id)

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(20), primary_key=False)
    model = db.Column(db.String(20), primary_key=False)
    stock = db.Column(db.Integer, primary_key=False)

    def __repr__(self):
        return '<Car %r %r>' % (self.manufacture , self.id)