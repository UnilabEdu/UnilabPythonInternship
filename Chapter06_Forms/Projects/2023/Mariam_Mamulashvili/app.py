from flask import Flask, render_template, request, url_for
from forms import AddMediaForm

flask_app = Flask(__name__)
flask_app.config["SECRET_KEY"] = "sdjkafhjfhfwerhgiuweh"


is_admin = True


product_dictionary = {
    "image": [
        {"title": "Explosion", "description": "explosion of car ", "image": "https://c8.alamy.com/comp/R7A9T5/car-on-fire-car-explosion-side-view-R7A9T5.jpg"},
        {"title": "Explosion", "description": "explosion of car ", "image": "https://c8.alamy.com/comp/R7A9T5/car-on-fire-car-explosion-side-view-R7A9T5.jpg"},
        {"title": "Explosion", "description": "explosion of car ", "image": "https://c8.alamy.com/comp/R7A9T5/car-on-fire-car-explosion-side-view-R7A9T5.jpg"},
        {"title": "Explosion", "description": "explosion of car ", "image": "https://c8.alamy.com/comp/R7A9T5/car-on-fire-car-explosion-side-view-R7A9T5.jpg"}
    ], 
    "video": [
        {"title": "Explosion", "description": "explosion of car ", "image": "https://www.youtube.com/watch?v=DGuDFUiyJp4"},
        {"title": "Explosion", "description": "explosion of car ", "image": "https://www.youtube.com/watch?v=DGuDFUiyJp4"}
    ]

}
@flask_app.route('/')
def home():
    print(url_for('home'))
    return render_template('home.html', is_admin=is_admin)

@flask_app.route('/gimbal/')
def gimbal():
    return render_template('gimbal.html', is_admin=is_admin, product_dictionary=product_dictionary)

@flask_app.route('/about/')
def about():
    print(url_for('about'))
    return render_template('about.html', is_admin=is_admin)

@flask_app.route('/add_media/', methods=['GET', 'POST'])
def add_media():

    form = AddMediaForm()
    if form.validate_on_submit():
        category : form.product_category.data
        product_dict = {
            "title": form.product_name.data,
            "description": form.description.data,
            "image": form.product_image.data,
      
        }
        product_dictionary[category].append(product_dict)
    else:
        print('Form not validated')
    return render_template('add_media.html', is_admin=is_admin, form=form)


@flask_app.route('/contact/')
def contact():
    print(url_for('contact'))
    return render_template('contact.html', is_admin=is_admin)

if __name__ == '__main__':
    flask_app.run(debug=True)