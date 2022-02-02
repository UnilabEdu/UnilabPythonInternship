from flask import Blueprint, render_template, redirect, url_for

main_blueprint = Blueprint('main',
                           __name__,
                           template_folder='templates/main')


@main_blueprint.route('/')
def main():
    return render_template("main.html")
