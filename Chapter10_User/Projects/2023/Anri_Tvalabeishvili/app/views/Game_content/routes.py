from flask import Blueprint, render_template
from app.views.Game_content.forms import GamesFilter
from app.models.product import Game


Game_content_blueprint = Blueprint("Game_content", __name__, template_folder="templates")






@Game_content_blueprint.route('/game_store', methods=["GET", "POST"])
def game_store():
    filter = GamesFilter()
    
    if filter.validate_on_submit():
        search = filter.search.data

        platform_PS5 = "PS5" if filter.platform_PS5.data else " "

        platform_PS4 = "PS4" if filter.platform_PS4.data else " "

        platform_XSX = "XSX" if filter.platform_XSX.data else " "
       
        platform_X1X = "X1X" if filter.platform_X1X.data else " "
 
        platform_X1S = "X1S" if filter.platform_X1S.data else " "

        platforms = [platform_PS5, platform_PS4, platform_XSX, platform_X1X, platform_X1S]


        if len(set(platforms)) == 1:
            platforms = ["PS5", "PS4", "XSX", "X1X", "X1S"]


    

        Exclusive = ["Yes"] if filter.Exclusive.data == "Yes" else ["Yes", "No"]


        user_price = list(map(int,filter.price.data.split("-")))



        if search:
            products = Game.query.\
            filter( Game.price > user_price[0],
                    Game.price < user_price[1],
                    Game.name.contains(search), 
                    Game.platform.in_(platforms),
                    Game.exclusive.in_(Exclusive)).all()

            return render_template("/Game_content/Page.html", products=products, filter=filter)
        
        else:

            products = Game.query.\
                filter(  Game.price > user_price[0], 
                         Game.price < user_price[1],
                         Game.platform.in_(platforms), 
                         Game.exclusive.in_(Exclusive)).all()

            return render_template("/Game_content/Page.html", products=products, filter=filter)




    products = Game.query.all()

    return render_template("/Game_content/Page.html", products=products, filter=filter)


