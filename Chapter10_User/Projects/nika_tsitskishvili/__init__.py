from views import routes
from app import app
from views import home_blueprint, logout_blueprint, login_blueprint, reg_blueprint, data_blueprint
routes()
app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(login_blueprint, url_prefix="/login")
app.register_blueprint(logout_blueprint, url_prefix="/logout")
app.register_blueprint(reg_blueprint, url_prefix="/register")
app.register_blueprint(data_blueprint, url_prefix="/data")


