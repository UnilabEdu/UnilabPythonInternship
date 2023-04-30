from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField, RadioField



class GamesFilter(FlaskForm):
    search = StringField("Search")

    platform_PS5 = BooleanField("Playstation 5")
    platform_PS4 = BooleanField("Playstation 4")
    platform_XSX = BooleanField("Xbox Series X")
    platform_X1X = BooleanField("Xbox One X")
    platform_X1S = BooleanField("Xbox One S")



    Exclusive = RadioField(choices=[('all','Everithing'),('Yes','Yes')], default="all")

    price = RadioField(choices=[('0-250','0₾ - 250₾'),
    ('0-20','0₾ - 20₾'),('20-40','20₾ - 40₾'), 
    ('40-60','40₾ - 60₾'),('60-80','60₾ - 80₾'),
    ('80-100','80₾ - 100₾'),('100-250','100₾ - 250₾'),], default="0-250")


    submit = SubmitField()