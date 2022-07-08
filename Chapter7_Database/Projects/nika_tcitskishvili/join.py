from app import app, db
from database import create_database
from api import api, Subject

@app.before_first_request
def before_first_request():
    db.create_all()
    create_database()
api.add_resource(Subject, '/subject/<int:id>')
if __name__ == "__main__":
    app.run(debug=True)