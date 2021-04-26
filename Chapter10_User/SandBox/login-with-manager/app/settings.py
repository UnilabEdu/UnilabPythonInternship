
APP_NAME = "DEMO APP"

# SQLAlchemy CONFIG
SQLALCHEMY_TRACK_MODIFICATIONS = False

# FLASK-USER CFG
USER_APP_NAME = APP_NAME

# Flask-User settings
USER_APP_NAME = APP_NAME
USER_ENABLE_EMAIL = True  # Register with Email
USER_ENABLE_USERNAME = True  # Register and Login with username
USER_ENABLE_CHANGE_USERNAME = True  # Allow users to change their username
USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password

USER_ENABLE_CONFIRM_EMAIL = False  # Force users to confirm their email
USER_ENABLE_FORGOT_PASSWORD = False  # Allow users to reset their passwords

USER_ENABLE_REGISTRATION = True  # Allow new users to register
USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:

USER_AFTER_LOGIN_ENDPOINT = 'user.profile'
USER_AFTER_LOGOUT_ENDPOINT = 'main.home_page'