from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Petition, User, Role


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database Creation in Progress...")

    db.drop_all()
    db.create_all()

    click.echo("Database Created!")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating Initial Entries...")

    admin_role = Role(id=1, user_role="Admin")
    admin_role.create()

    user_role = Role(id=2, user_role="User")
    user_role.create()

    user = User(
        id=1,
        username="b_gogeishvili",
        name="Beso",
        surname="Gogeishvili",
        email="gogeishvilib@gmail.com",
        sex="male",
        password="qwerty",
        role_id=1
    )

    petition1 = Petition(
        id=1,
        user_id=1,
        name="კუპატა",
        title="დაიდგას კუპატას ძეგლი ქალაქ ბათუმში",
        address="კულტურისა და ძეგლთა დაცვის სამინისტრო",
        description="""კუპატა, ჰაჩიკო, ლაიკა, ბალტო და სხვა ძაღლები, რომლებიც მსოფლიომ გაიცნო.
                ჩვენი კუპატა მთელმა საქართველომ სოციალურ ქსელში გავრცელებული ვიდეოთი გაიცნო, რომელშიც ის ბავშვებს
                ზებრაზე გადასვლაში ეხმარებოდა და ავტომობილის უყურადღებო მძღოლებს უყეფდა.
                ამის შემდეგ ცუგა ბათუმში შენობის კედელზე უზარმაზარი სტენსილითაც გამოსახეს. აჭარის ტურიზმისა და
                კურორტების დეპარტამენტის თანამშრომლებმა სახლი უყიდეს, მალევე კი ვარსკვლავიც გაუხსნეს, როგორც ხალხის
                რჩეულს.
                ზემოთ ჩამოთვლილი ძაღლებიდან ბევრი მათგანის ძეგლი უკვე დგას მსოფლიოს სხვადასხვა ქალაქში, ჩვენი კუპატა
                ვისზე ნაკლები იყო?
                ამიტომ მგონი ცუდი იდეა არ არის, დაიდგას ძეგლი ბათუმში, თუნდაც იმ გადასასვლელთან ან იმ უბანში სადაც
                ცხოვრობდა.
                დაგვეხმარე საკმარისი ხელმოწერების დაგროვებაში!""",
        short_description="ცუდი იდეა არ არის, დაიდგას ძეგლი ბათუმში, თუნდაც იმ გადასასვლელთან ან იმ უბანში სადაც კუპატა ცხოვრობდა."
                          "დაგვეხმარე საკმარისი ხმების მოგროვებაში!",
        url_name="kupata",
        img1="./static/assets/kupata/kupata_lovely.jpg",
        img2="./static/assets/kupata/kupata_art01.jpg",
        img3="./static/assets/kupata/kupata_art00.jpg",
        img4="./static/assets/kupata/kupata01.jpg",
        img5="./static/assets/kupata/kupata00.jpg",
        method="upload",
        goal=1243,
        votes=0
    )

    petition2 = Petition(
        id=2,
        user_id=1,
        name="ჯანსაღი კვება",
        title="ჯანსაღი კვება ყველა მოსწავლეს",
        address="განათლებისა და მეცნიერების სამინისტრო",
        description="""წინამდებარე პეტიციაზე ხელისმომწერნი მოვითხოვთ: დაუყოვნებლივ შეწყდეს სკოლის ბუფეტებში ჯანმრთელობისთვის 
                    მავნე საკვებით ვაჭრობა და სახელმწიფომ დააფინანსოს სკოლებში ჯანსაღი კვების პროგრამა.
                    დღეისათვის გაკვეთილებს უმეტესად მშიერი ბავშვები ესწრებიან. სახელმწიფო ვერ უზრუნველყოფს მოსწავლეთა კვებას. 
                    ბევრ ოჯახს არ აქვს შესაძლებლობა შვილს სახლიდან გაატანოს საკვები, რაც ზრდის ბავშვებს შორის უთანასწორობას. 
                    ბევრ სკოლაში არ არსებობს ბუფეტი. სადაც ბუფეტი ფუნქციონირებს, ეს იმის ხარჯზე, 
                    რომ სკოლის სივრცე ნაქირავები აქვს კერძო პირს და ბუფეტის ნაცვლად იქ გახსნილი აქვს მაღაზია, 
                    სადაც ჯანმრთელობისთვის ზიანის მომტანი პროდუქტებით ვაჭრობს. ე.წ ბუფეტში იყიდება გაზიანი სასმელები, მდარე, 
                    საეჭვო ხარისხის ტკბილეული და ცომეული, რაც ეწინააღმდეგება განათლებისა და მეცნიერების მინისტრის ბრძანება N410-ს, 
                    რომლითაც განსაზღვრულია სასკოლო კვების აკრძალული პროდუქტების ჩამონათვალი (საღეჭი რეზინი, კანფეტები, ჩიფსები, 
                    ჟელიბონი და ა.შ.)""",
        short_description="განათლების სამინისტრომ დაჩქარებული წესით დანერგოს ჯანსაღი სასკოლო კვების პროგრამა."
                          "მუშაობის პროცესი გახადოს გამჭვირვალე და ჩაგვაყენოს საქმის კურსში, რას აპირებს სახელმწიფო ამ მიმართულებით.",
        url_name="jansagi-kveba",
        img1="https://healthyschoolscampaign.org/dev/wp-content/uploads/2020/01/Judging-Cooking-up-Change-2015-92_Blog.jpg",
        img2="https://www.pewtrusts.org/-/media/post-launch-images/2016/10/school_strategies_promote_healthy_eating/school_strategies_promote_healthy_eating_16x9.jpg",
        img3="https://againstallgrain.com/wp-content/uploads/2020/08/lunchbox-blog-scaled.jpg",
        img4="https://www.brookings.edu/wp-content/uploads/2017/05/rtr2jl3x.jpg",
        img5="https://familydoctor.org/wp-content/uploads/2011/01/35992525_l.jpg",
        method="link",
        goal=243,
        votes=243
    )

    petition1.create()
    petition2.create()
    user.create()

    click.echo("Entries Created!")
