from flask import Blueprint, render_template
from app.views.Gift_content.forms import GiftFilter
from app.models.product import Gift

Gift_content_blueprint = Blueprint("Gift_content", __name__, template_folder="templates")

# ✔
@Gift_content_blueprint.route('/gift_Cards', methods=["GET", "POST"])
def gift_Cards():
    filter = GiftFilter()
    
    if filter.validate_on_submit():
        platform_PSGC = "PSGC" if filter.platform_PS_GC.data else " "

        platform_PSPL = "PSPL" if filter.platform_PS_Plus.data else " "

        platform_XBGC = "XBGC" if filter.platform_X_GC.data else " "
       
        platform_XBGP = "XBGP" if filter.platform_X_UP.data else " "
 

        if len(set([platform_PSGC, platform_PSPL, platform_XBGC, platform_XBGP])) == 1:
            platform_PSGC = "PSGC"
            platform_PSPL = "PSPL"
            platform_XBGC = "XBGC"
            platform_XBGP = "XBGP"

        

        region_1 = "USA" if filter.region_1.data else " "

        region_2 = "UK" if filter.region_2.data else " "

        region_3 = "Italy" if filter.region_3.data else " "
       
        region_4 = "Poland" if filter.region_4.data else " "
 
        region_5 = "Germany" if filter.region_5.data else " "

        region_6 = "Czech Republic" if filter.region_6.data else " "


        if len(set([region_1, region_2, region_3, region_4, region_5, region_6])) == 1:
            region_1 = "USA"
            region_2 = "UK"
            region_3 = "Italy"
            region_4 = "Poland"
            region_5 = "Germany"
            region_6 = "Czech Republic"    

  
        products = Gift.query.\
                filter(Gift.type.in_([platform_PSGC, platform_PSPL, platform_XBGC, platform_XBGP]), Gift.region.in_([region_1, region_2, region_3, region_4, region_5, region_6])).all()

        return render_template("/Gift_content/Page.html", products=products, filter = filter) 

    products = Gift.query.all()
    return render_template("/Gift_content/Page.html", products=products, filter = filter)


