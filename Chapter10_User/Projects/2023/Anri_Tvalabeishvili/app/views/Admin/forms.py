from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class Admin_navigation(FlaskForm):
    categoty = SelectField("categoty" , choices=[("Game", "Game"), ("Gift","Gift")], default="Game")
    categoty_update = SelectField("categoty" , choices=[("Game", "Game"), ("Gift","Gift"),("User","User")], default="Game")




class Admin_Game_Add(FlaskForm):

    game_name = StringField("Name:")
    game_price = IntegerField("Price:")
    game_condition = SelectField("Condition:", choices=[("New", "New"), ("Used","Used")])
    game_platform = SelectField("Platform:", choices=[("PS5", "PS5"), ("PS4","PS4"), ("XSX","XSX"), ("X1X","X1X"), ("X1S","X1S")])
    game_exclusive = SelectField("Exclusive:", choices=[("Yes", "Yes"), ("No", "No")])
    game_quantity = IntegerField("Quantity:")
    game_img = StringField("Img Link:")


    game_sumbit = SubmitField()




class Admin_Gift_Add(FlaskForm):


    gift_name = StringField("Name:")
    gift_price = IntegerField("Price:")
    gift_region = SelectField("Region:", choices=[("USA", "United States"), ("UK","United Kingdom"), ("Italy", "Italy"), ("Poland", "Poland"), ("Germany", "Germany"),("Czech Republic", "Czech Republic"),])
    gift_type = SelectField("Type:", choices=[("PSGC", "PSGC"), ("PSPL","PSPL"), ("XBGC", "XBGC"), ("XBGP", "XBGP")])
    gift_img = StringField("Img link")


    gift_sumbit = SubmitField()

    









class Admin_content_Update(FlaskForm):
    ID_search = StringField("ID:", validators=[DataRequired()])






class Admin_Game_Update(FlaskForm):

    game_name_update = StringField("Name:")
    game_price_update = IntegerField("Price:")
    game_condition_update = SelectField("Condition:", choices=[("New", "New"), ("Used","Used")])
    game_platform_update = SelectField("Platform:", choices=[("PS5", "PS5"), ("PS4","PS4"), ("XSX","XSX"), ("X1X","X1X"), ("X1S","X1S")])
    game_exclusive_update = SelectField("Exclusive:", choices=[("Yes", "Yes"), ("No", "No")])
    game_quantity_update = IntegerField("Quantity:")
    game_img_update = StringField("Img Link:")


    game_sumbit_update = SubmitField()




class Admin_Gift_Update(FlaskForm):


    gift_name_update = StringField("Name:")
    gift_price_update = IntegerField("Price:")
    gift_region_update = SelectField("Region:", choices=[("USA", "United States"), ("UK","United Kingdom"), ("Italy", "Italy"), ("Poland", "Poland"), ("Germany", "Germany"),("Czech Republic", "Czech Republic"),])
    gift_type_update = SelectField("Type:", choices=[("PSGC", "PSGC"), ("PSPL","PSPL"), ("XBGC", "XBGC"), ("XBGP", "XBGP")])
    gift_img_update = StringField("Img link")


    gift_sumbit_update = SubmitField()