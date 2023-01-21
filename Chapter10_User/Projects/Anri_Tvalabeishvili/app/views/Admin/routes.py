from flask import Blueprint, render_template, redirect
from app.models.product import Game, Gift
from app.models.user import User
from app.views.Admin.forms import Admin_navigation, Admin_Game_Add, Admin_Gift_Add , Admin_content_Update, Admin_Game_Update, Admin_Gift_Update
from app.extensions import db
from app.utils import admin_required


Admin_content_blueprint = Blueprint("Admin_content", __name__, template_folder="templates")

# ეს როური მხოლოდ მაშინ უნდა ჩანდეს თუ ადმინი არის შემობრძანებული
@Admin_content_blueprint.route('/admin', methods=["GET", "POST"])
@admin_required
def admin():
    
    navigation_form = Admin_navigation()
    add_game_form = Admin_Game_Add()
    add_gift_form = Admin_Gift_Add()
    update_content_form = Admin_content_Update()
    update_game_form = Admin_Game_Update()
    update_gift_form = Admin_Gift_Update()

    if add_game_form.validate_on_submit():
        game_name = add_game_form.game_name.data
        game_price = add_game_form.game_price.data
        game_condition = add_game_form.game_condition.data
        game_platform = add_game_form.game_platform.data
        game_exclusive = add_game_form.game_exclusive.data
        game_quantity = add_game_form.game_quantity.data
        game_img = add_game_form.game_img.data

        game_item = Game(name=game_name, platform=game_platform, condition=game_condition,
                          exclusive=game_exclusive, price=game_price, cuantity=game_quantity, img=game_img)
        game_item.create()
        game_item.save()


    if add_gift_form.validate_on_submit():
        gift_name = add_gift_form.gift_name.data
        gift_price = add_gift_form.gift_price.data
        gift_region = add_gift_form.gift_region.data
        gift_type = add_gift_form.gift_type.data
        gift_img = add_gift_form.gift_img.data

        gist_item = Gift(name=gift_name, type=gift_type,
                         price=gift_price, img=gift_img, region=gift_region)

        gist_item.create()
        gist_item.save()

    
    category = navigation_form.categoty_update.data
    seach_ID = update_content_form.ID_search.data

    if update_game_form.validate_on_submit() and category == "Game":
         
        new_game_name = update_game_form.game_name_update.data
        new_game_price = update_game_form.game_price_update.data
        new_game_condition = update_game_form.game_condition_update.data
        new_game_platform = update_game_form.game_platform_update.data
        new_game_exclusive = update_game_form.game_exclusive_update.data
        new_game_quantity = update_game_form.game_quantity_update.data
        new_game_img = update_game_form.game_img_update.data

        


        Game.query.filter_by(id=seach_ID).update({"name":new_game_name , "platform":new_game_platform, "condition":new_game_condition, 
        "exclusive":new_game_exclusive, "price": new_game_price , "cuantity":new_game_quantity , "img": new_game_img   })

        db.session.commit()




        
        return render_template("/Admin/admin.html", add_game=add_game_form, add_gift=add_gift_form, 
        nav=navigation_form, update_content=update_content_form, update_game = update_game_form , update_gift = update_gift_form,)


    # იგივე იქნება gift ისთვისაც

    return render_template("/Admin/admin.html", add_game=add_game_form, add_gift=add_gift_form, 
    nav=navigation_form, update_content=update_content_form, update_game = update_game_form , update_gift = update_gift_form )

