from app import app
from app.routes import list_pages, auth, success_register, logoff
from app.admin.admin_model import AdminModelView

if __name__ == '__main__':
    app.run(port=5080, debug=True)
