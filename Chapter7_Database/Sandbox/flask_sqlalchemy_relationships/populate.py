from models import db, Worker, Order

temo = Worker.query.filter_by(name='Temo').first()

order1 = Order("კარპეს ქათმის ფრთები", temo.id)
order2 = Order("ქარის ლუპი", temo.id)

db.session.add_all([order1, order2])
db.session.commit()

temo = Worker.query.filter_by(name='Temo').first()

temo.report_orders()