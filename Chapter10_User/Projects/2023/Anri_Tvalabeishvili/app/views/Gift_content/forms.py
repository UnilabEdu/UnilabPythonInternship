from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField


class GiftFilter(FlaskForm):
    
    platform_PS_GC = BooleanField("Playstation Gift Card")
    platform_PS_Plus = BooleanField("Playstation Plus")
    platform_X_GC = BooleanField("Xbox Gift Card")
    platform_X_UP = BooleanField("Xbox Game Pass")



    region_1 = BooleanField("United States")
    region_2 = BooleanField("United Kingdom")
    region_3 = BooleanField("Italy")
    region_4 = BooleanField("Poland")
    region_5 = BooleanField("Germany")
    region_6 = BooleanField("Czech Republic")



    submit = SubmitField()