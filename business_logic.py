from models import db, Car, User

def save_car_booking(data):
    print(data)
    car = Car(
        car=data['car'],
        from_date=data['from_date'],
        to_date=data['to_date']
    )
    db.session.add(car)
    db.session.commit()

def get_car_booking():
    return Car.query.all()


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
                mobile_number=data['mobile_number']
            )
            db.session.add(user)
            db.session.commit()
            return True
        else:
            raise Exception('Paroles nesakrīt!')
    elif email_exist == True and data['password'] != data['password_confirm']:
        raise Exception('Paroles nesakrīt un E-pasts ir aizņemts!')
    else:
        raise Exception('E-pasts ir aizņemts!')