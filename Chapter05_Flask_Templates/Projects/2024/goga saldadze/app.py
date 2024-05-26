from flask import Flask, render_template

app =Flask(__name__)


prod_list =[ {
    "name":"acer laptop" , 
    "description": "i7 32ram",
    "img":"https://assets3.razerzone.com/2qIEzE6PovR0jcvcBUI6HVJQVKM=/300x300/https%3A%2F%2Fhybrismediaprod.blob.core.windows.net%2Fsys-master-phoenix-images-container%2Fhaf%2Fh7b%2F9720377704478%2Fblade14-p10-black-500x500.png"
 },
{
    "name":"razer laptop" , 
    "description": "i9 32ram",
    "img":"https://assets3.razerzone.com/2qIEzE6PovR0jcvcBUI6HVJQVKM=/300x300/https%3A%2F%2Fhybrismediaprod.blob.core.windows.net%2Fsys-master-phoenix-images-container%2Fhaf%2Fh7b%2F9720377704478%2Fblade14-p10-black-500x500.png"
},
{
    "name":"asus laptop" , 
    "description": "i5 32ram",
    "img":"https://assets3.razerzone.com/2qIEzE6PovR0jcvcBUI6HVJQVKM=/300x300/https%3A%2F%2Fhybrismediaprod.blob.core.windows.net%2Fsys-master-phoenix-images-container%2Fhaf%2Fh7b%2F9720377704478%2Fblade14-p10-black-500x500.png"
},
{
    "name":"dell laptop" , 
    "description": "i3 32ram",
    "img":"https://assets3.razerzone.com/2qIEzE6PovR0jcvcBUI6HVJQVKM=/300x300/https%3A%2F%2Fhybrismediaprod.blob.core.windows.net%2Fsys-master-phoenix-images-container%2Fhaf%2Fh7b%2F9720377704478%2Fblade14-p10-black-500x500.png"
} 
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/materials")
def materials():
    return render_template("materials.html")

@app.route("/products")
def products():
    return render_template("products.html", prod=prod_list)

@app.route("/products/<int:id>")
def view_product(id):
    picked_product= prod_list[id]
    return render_template("viewproduct.html",specprod=prod_list[id])



if __name__ == "__main__":
    app.run(debug=True)