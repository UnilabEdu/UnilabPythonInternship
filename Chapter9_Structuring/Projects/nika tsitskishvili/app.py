from project_one import create_application
from flask_migrate import Migrate
from project_one.extensions import db
app = create_application()
migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(debug=True)


