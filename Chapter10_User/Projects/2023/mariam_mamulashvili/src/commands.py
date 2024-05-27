from flask.cli import with_appcontext
import click

from src.models import User, Product, Contact, Works
from src.extensions import db

def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    click.echo("Creating admins")
    user1 = User(username="admin", password="admin123")
    user1.password = "admin123" 
    user2 = User(username="admin2", password="admin456")
    user1.create()
    user2.create()

    click.echo("Creating products")
    media1 = Product(product_name="gimbal", description="gimbal for camera", product_category="image", page_category="gimbal", product_image="gimbal1.jpg")
    media2 = Product(product_name="gimbal", description="gimbal for camera", product_category="image", page_category="gimbal", product_image="gimbal2.jpg")
    media3 = Product(product_name="gimbal", description="gimbal for camera", product_category="image", page_category="gimbal", product_image="gimba3.jpg")
    media4 = Product(product_name="atmospherics", description="atmospherics", product_category="image", page_category="atmospherics", product_image="atmospherics1.jpg")
    media5 = Product(product_name="atmospherics", description="atmospherics", product_category="image", page_category="atmospherics", product_image="atmospherics2.jpg")
    media6 = Product(product_name="pyrotechnics", description="atmospherics", product_category="image", page_category="pyrotechnics", product_image="pyro1.jpg")
    media7 = Product(product_name="pyrotechnics", description="atmospherics", product_category="image", page_category="pyrotechnics", product_image="pyro2.jpg")
    media8 = Product(product_name="model_making", description="model_making", product_category="image", page_category="model_making", product_image="model_making1.jpg")
    media9 = Product(product_name="model_making", description="model_making", product_category="image", page_category="model_making", product_image="model_making2.jpg")
    media10 = Product(product_name="pyrotechnics", description="atmospherics", product_category="video", page_category="pyrotechnics", product_image="pyrovideo1.mp4")
    media11 = Product(product_name="pyrotechnics", description="atmospherics", product_category="video", page_category="pyrotechnics", product_image="pyrovideo2.mp4")
    media2.create()
    media3.create()
    media4.create()
    media5.create()
    media6.create()
    media7.create()
    media8.create()
    media9.create()
    media10.create()
    media11.create()
    media1.create()

    click.echo("Creating gallery")
    image1 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery1.jpg")
    image2 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery2.jpg")
    image3 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery3.jpg")
    image4 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery4.jpg")
    image5 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery5.jpg")
    image6 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery6.jpg")
    image7 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery7.jpg")
    image8 =  Product(product_name="image", description="gallery-img", product_category="image", page_category="gallery", product_image="gallery8.jpg")
    image1.create()
    image2.create()
    image3.create()
    image4.create()
    image5.create()
    image6.create()
    image7.create()
    image8.create()



    click.echo("Creating works")
    works1 = Works(product_name="Lady of heaven", description="Two stories separated by 1400 years. After losing his mother in the midst of a war-torn country, an Iraqi child, learns the importance and power of patience by discovering the historical story of Lady Fatima and her suffering",
                product_category="Action, Drama, History", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/597961611747135-p2rwcuqi2o2z8ggbvhgi91b2kcb5fr40wnim38ckts.jpg", release_year="2021", director="Eli King", product_video="Lady of heaven.mp4")
    works2= Works(product_name = "Dark Light", description =  "A woman returns to her family home and discovers it to be inhabited by monsters",
                  product_category = "Horror, Sci-Fi, Thriller", product_image= "https://sarkestudio.com/wp-content/uploads/elementor/thumbs/15.-Dark-Light-2019-p31n7rldnsuln3cj7rlcg63nvq5cpzyjtv7a4ydai8.jpg", release_year = "2019", director = "Padraig Reynolds", product_video = "Dark Light.mp4" )
    works3= Works(product_name = "Sye Raa Narasimha Reddy", description= "A historical action epic inspired by the life of Uyyalawada Narasimha Reddy, who revolted against the atrocities of East India Company 10 years before the Sepoy Mutiny.",
                  product_category = "Action, Drama, History", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/16.-Sye-Raa-Narasimha-Reddy-2019-1-p31o202hhy8n3jfgnu3bnjffrx4ebhzpzinjvdjecw.jpg",
                  release_year = "2019", director="Surrender Reddy", product_video = "Sye Raa.mp4" )
    works4= Works(product_name = "Special Ops 1.5: The Himmat Story", description= "After the 2001 Parliament attack, a young and idealistic RA&W officer had a theory. In 2003, he had a mystery. This is the story of Himmat Singh",
                  product_category = "Action, Crime, Drama", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/Poster-e1637926623818-pgmpf6tmhdc0d3gnlfevl1b88z67pf0igjhcs228a8.png",
                  release_year = "2021", director="Neeraj Pandey, Shivam Nair", product_video = "Specials.mp4" )
    works5= Works(product_name = "Inside Edge", description= "Inside Edge is the story of the Mumbai Mavericks, a T20 cricket franchise playing in the Powerplay League. ",
                  product_category = "Drama, Sport", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/17.-Inside-Edge-2019-p31n7orv3aqqo9gmo8dgqota3kj92wncth8tp4hh0w.jpg",
                  release_year = "2018", director="Karan Anshuman", product_video = "Inside Edge.mp4" )
    works6= Works(product_name = "Daddy’s Girl", description= "A young woman held captive by her stepfather becomes the focus of a female vigilante.",
                  product_category = "Crime, Horror, Thriller", product_image="https://sarkestudio.com/wp-content/uploads/elementor/thumbs/11.-Daddys-Girl-2018--p31n6ygdrxqpn6iuxwzwsvgdgs4z3dqvduz89dkhv4.jpg",
                  release_year = "2018", director="Julian Richards", product_video = "Daddy's Girl.mp4" )
    

    works1.create()
    works2.create()
    works3.create()
    works4.create()
    works5.create()
    works6.create()

@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Database creation in porgress")
    init_db()
    click.echo("Database created")




@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()




    
   








