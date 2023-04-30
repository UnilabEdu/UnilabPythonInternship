from models import db, Bike, Worker, Order

ucha = Worker.query.filter_by(name="Ucha").first()

order1 = Order("Chicken wings", ucha.id)
order2 = Order("Cheesburger with fries", ucha.id)
db.session.add_all([order1,order2])
db.session.commit()

ucha.report_orders()