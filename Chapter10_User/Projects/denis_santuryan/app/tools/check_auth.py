def check_auth():
    """
    returns True if user is logged in
    else returns False
    """
    from flask_login import current_user

    try:
        if current_user.is_authenticated:
            return True
    except AttributeError:
        return False
