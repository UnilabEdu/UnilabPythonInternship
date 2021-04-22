from Elektronyx import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView


"""
User Model
"""
class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(32), nullable=False, unique=True, index=True)
    password = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean())

    def __init__(self, email, username, password, is_admin):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.is_admin = is_admin;

    @classmethod
    def find_by_email(cls, email):
        email = cls.query.filter_by(email=email).first()
        if email:
            return email

    @classmethod
    def find_by_user(cls, user):
        user = cls.query.filter_by(username=user).first()
        if user:
            return user

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


"""
Flask-Admin Models
"""
class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


"""
Product models
"""
class Product():

    @classmethod
    def get_all(cls):
        products = cls.query.all()
        return products

    @classmethod
    def find_by_name(cls, model):
        found_product = cls.query.filter_by(model=model).first()
        return found_product


class Case(db.Model, Product):

    __tablename__ = "case"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    color = db.Column(db.String)
    height = db.Column(db.String)
    width = db.Column(db.String)
    depth = db.Column(db.String)

    def __init__(self, manufacturer, model, color, height, width, depth, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.depth = depth
        self.width = width
        self.height = height
        self.quantity = quantity
        self.price = price
        self.img = img


class PSU(db.Model, Product):

    __tablename__ = "PSU"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    efficiency = db.Column(db.String)
    wattage = db.Column(db.Integer)

    def __init__(self, manufacturer, model, efficiency, wattage, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.efficiency = efficiency
        self.wattage = wattage
        self.quantity = quantity
        self.price = price
        self.img = img


class Motherboard(db.Model, Product):

    __tablename__ = "motherboard"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    socket_type = db.Column(db.String)
    memory_type = db.Column(db.String)
    memory_slots = db.Column(db.Integer)
    max_memory = db.Column(db.Integer)

    def __init__(self, manufacturer, model, socket_type, memory_type, memory_slots, max_memory, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.socket_type = socket_type
        self.memory_type = memory_type
        self.memory_slots = memory_slots
        self.max_memory = max_memory
        self.quantity = quantity
        self.price = price
        self.img = img


class CPU(db.Model, Product):

    __tablename__ = "CPU"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    socket_type = db.Column(db.String)
    core_count = db.Column(db.Integer)
    core_clock = db.Column(db.String)
    power_draw = db.Column(db.Integer)

    def __init__(self, manufacturer, model, socket_type, core_count, core_clock, power_draw, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.socket_type = socket_type
        self.core_count = core_count
        self.core_clock = core_clock
        self.power_draw = power_draw
        self.quantity = quantity
        self.price = price
        self.img = img


class GPU(db.Model, Product):

    __tablename__ = "GPU"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    vram = db.Column(db.Integer)
    vram_type = db.Column(db.String)
    power_draw = db.Column(db.Integer)
    length = db.Column(db.String)

    def __init__(self, manufacturer, model, vram, vram_type, power_draw, length, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.vram = vram
        self.vram_type = vram_type
        self.power_draw = power_draw
        self.length = length
        self.quantity = quantity
        self.price = price
        self.img = img


class RAM(db.Model, Product):

    __tablename__ = "RAM"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    memory_type = db.Column(db.String)
    memory_speed = db.Column(db.Integer)
    memory_size = db.Column(db.String)

    def __init__(self, manufacturer, model, memory_type, memory_speed, memory_size, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.memory_type = memory_type
        self.memory_speed = memory_speed
        self.memory_size = memory_size
        self.quantity = quantity
        self.price = price
        self.img = img


class Storage(db.Model, Product):

    __tablename__ = "storage"

    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    img = db.Column(db.String)

    storage_type = db.Column(db.String)
    storage_capacity = db.Column(db.String)

    def __init__(self, manufacturer, model, storage_type, storage_capacity, price, quantity, img):
        self.manufacturer = manufacturer
        self.model = model
        self.storage_type = storage_type
        self.storage_capacity = storage_capacity
        self.quantity = quantity
        self.price = price
        self.img = img