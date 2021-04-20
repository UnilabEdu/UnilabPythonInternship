from app import app
from app.routes import list_pages, auth, success_register, logoff


if __name__ == '__main__':
    app.run(port=5080, debug=True)
