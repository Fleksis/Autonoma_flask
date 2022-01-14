from models import db, UserCar, User, Car
from flask import session


def save_car_booking(data, id):
    car = UserCar(
        car=data['car'],
        from_date=data['from_date'],
        to_date=data['to_date'],
        owner_id=id
    )
    db.session.add(car)
    db.session.commit()

def get_user_car_booking(id):
    cars = UserCar.query.filter(UserCar.owner_id == id).all()
    if cars != None:
        return cars
    else:
        raise Exception('Lūdzu pieslēdzaties!')

def save_user_registration(data):
    email_exist = (User.query.filter(User.email == data['email']).first() != None)
    if email_exist == False:
        if data['password'] == data['password_confirm']:
            user = User(
                firstname=data['firstname'],
                lastname=data['lastname'],
                email=data['email'],
                password=data['password'],
                address=data['address'],
                mobile_number=data['mobile_number'],
                role="user"
            )
            db.session.add(user)
            db.session.commit()
            session['user'] = user.id
            return True
        else:
            raise Exception('Paroles nesakrīt!')
    elif email_exist == True and data['password'] != data['password_confirm']:
        raise Exception('Paroles nesakrīt un E-pasts ir aizņemts!')
    else:
        raise Exception('E-pasts ir aizņemts!')

def compare_user_login(data):
    user = User.query.filter(User.email == data['email']).first() # Iegūstam lietotāju kuram ir ievadītais e-pasts
    if user != None and user.password == data['password']:
        session['user'] = user.id
        return True
    else:
        raise Exception("Nepareizs epasts vai parole!")

def get_user_data(id):
    return User.query.filter(User.id == id).first()

def get_all_users_cars():
    data = []
    for car in UserCar.query.all():
        data.append([car, get_user_data(car.owner_id)])
    return data


def is_user_admin(id):
    try:
        return True if get_user_data(id).role == "admin" else False
    except Exception as e:
        raise Exception("Lietotajs nav pieslēdzies sistēmai/Nav pieeja šai lapai")

def is_user_logged():
    try:
        return True if get_user_data(session['user']) else False
    except:
        raise Exception("Lietotajs nav pieslēdzies sistēmai/Nav pieeja šai lapai")

def set_status_code(car_id, status_code):
    try:
        UserCar.query.get(car_id).booked_status = status_code
        db.session.commit()
        return UserCar
    except:
        raise Exception("Notika kļūda!")

def set_car_stock(data):
    car = Car(
        manufacture=data['manufacture'],
        model=data['model'],
        stock=data['stock']
    )
