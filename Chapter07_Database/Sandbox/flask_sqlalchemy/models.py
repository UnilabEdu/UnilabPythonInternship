from app import db


#################################
#   ONE TO ONE relationships   #
################################
class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'))
    category = db.relationship("ProductCategory", uselist=False)

    def __repr__(self):
        return f"{self.name} - {self.category}"


class ProductCategory(db.Model):

    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


#################################
#   ONE TO MANY relationships   #
################################
class Teacher(db.Model):

    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    students = db.relationship("Student", backref="teacher")


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    course = db.Column(db.String)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))


#################################
#   MANY TO MANY relationships #
################################

# დამხმარე თეიბლი რომელიც აკავშირეს Actor-ს და Film-ს, ამას ხშირად ეძახიან ასოციაციის თეიბლს (Association Table)
class ActorFilm(db.Model):

    __tablename__ = "actors_films"

    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    film_id = db.Column(db.Integer, db.ForeignKey("films.id"))


class Actor(db.Model):

    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # როდესაც გაქვს ასოციაციური თეიბლი, secondary-ში წერ მის __tablename__-ს
    films = db.relationship("Film", secondary="actors_films", backref="actors")

    def __repr__(self):
        return self.name


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

    def __repr__(self):
        return self.name


