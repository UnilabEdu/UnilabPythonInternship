from flask import render_template, request, redirect, url_for, flash, session
from app import app


@app.errorhandler(404)
def not_found(error):
    return 'Page Not Found', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Internal Server  Error', 500

@app.errorhandler(403)
def forbidden(error):
    return 'forbidden', 403


