from flask import Blueprint, render_template

error_pages = Blueprint('error', __name__)


@error_pages.app_errorhandler(404)
def error_404(error):
    '''
    Error for pages not found.
    '''
    # Notice how we return a tuple!
    return render_template('errors/404.html', error=error), 404


@error_pages.app_errorhandler(403)
def error_403(error):
    '''
    Error for trying to access something which is forbidden.
    Such as trying to update someone else's blog post.
    '''
    # Notice how we return a tuple!
    return render_template('errors/403.html', error=error), 403
