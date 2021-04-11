from app import db, UserModel

# Create
user = UserModel('temurchichua', 'temur.chichua@iliauni.edu.ge', 23, 'Georgia')
print(user.id)

db.session.add(user)
db.session.commit()

print(user.id)

# Read
users = UserModel.query.all()  # მიიღებს ბაზის მოდელით შენახული ყველა წევრის მნიშვნელობას

# ID-ით ამორჩევა
user_by_id = UserModel.query.get(2)  # get() გადავცემთ id-ს ინდექსს

# ფილტრები

user2 = UserModel.query.filter_by(username='user2').first()  # first() დააბრუნებს ობიექტის მხოლოდ პირველ ელემენტს.
# Update

# Read + Save

# Delete

user_by_id = UserModel.query.get(1)  # ამოვიღეთ id-ით მეორე ობიექტი ბაზიდან
db.session.delete(user_by_id)  # წავშალე ობიექტი სესიიდან
db.session.commit  # გადავიტანე სასეიაში შეტანილი ცვლილებები ბაზაში
