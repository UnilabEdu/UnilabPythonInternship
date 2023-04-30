from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
