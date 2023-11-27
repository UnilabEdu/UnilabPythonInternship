from flask import Flask
from string import ascii_lowercase
import os

app = Flask(__name__, template_folder='./templates')
app.config["SECRET_KEY"] = "flaskappkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TRACK_DATABASE_MODIFICATIONS"] = False

UPLOAD_PATH = os.path.join(app.root_path, "static", "assets")
UPLOADING_IMAGES = ["main_img", "left_img1", "left_img2", "right_img1", "right_img2"]

def to_english(word):
    
    alphabet = {"ა": "a","ბ": "b", "გ": "g", "დ": "d", "ე": "e", "ვ": "v", "ზ": "z", 
        "თ": "t", "ი": "i", "კ": "k", "ლ": "l","მ": "m","ნ": "n","ო": "o","პ": "p","ჟ": "zh",
        "რ": "r","ს": "s","ტ": "t","უ": "u","ფ": "f","ქ": "q","ღ": "gh","ყ": "y","შ": "sh",
        "ჩ": "ch","ც": "c","ძ": "dz","წ": "w","ხ": "x","ჯ": "j","ჰ": "h", " ": "-"}
        
    if word[0] not in ascii_lowercase:
        
        translated_word = ""

        for letter in word.lower():
            translated_word += alphabet[letter]

        return translated_word
    else:
        return word


data = { "petitions": [
    {
    "name": "კუპატა",
    "title": "ᲓᲐᲘᲓᲒᲐᲡ ᲙᲣᲞᲐᲢᲐᲡ ᲫᲔᲒᲚᲘ ᲥᲐᲚᲐᲥ ᲑᲐᲗᲣᲛᲨᲘ",
    "adress": "კულტურისა და ძეგლთა დაცვის სამინისტრო",
    "description": """კუპატა, ჰაჩიკო, ლაიკა, ბალტო და სხვა ძაღლები, რომლებიც მსოფლიომ გაიცნო.
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
    "short_description": "ცუდი იდეა არ არის, დაიდგას ძეგლი ბათუმში, თუნდაც იმ გადასასვლელთან ან იმ უბანში სადაც კუპატა ცხოვრობდა." 
                        "დაგვეხმარე საკმარისი ხმების მოგროვებაში!",
    "url_name": "kupata",
    "img1": "../static/assets/kupata/kupata_art00.jpg",
    "img2": "../static/assets/kupata/kupata_art01.jpg",
    "img3": "../static/assets/kupata/kupata_lovely.jpg",
    "img4": "../static/assets/kupata/kupata01.jpg",
    "img5": "../static/assets/kupata/kupata00.jpg",
    },
    {
    "name": "ჯანსაღი კვება",
    "title": "ᲯᲐᲜᲡᲐᲦᲘ ᲙᲕᲔᲑᲐ ᲧᲕᲔᲚᲐ ᲛᲝᲡᲬᲐᲕᲚᲔᲡ",
    "adress": "განათლებისა და მეცნიერების სამინისტრო",
    "description": """წინამდებარე პეტიციაზე ხელისმომწერნი მოვითხოვთ: დაუყოვნებლივ შეწყდეს სკოლის ბუფეტებში ჯანმრთელობისთვის 
                    მავნე საკვებით ვაჭრობა და სახელმწიფომ დააფინანსოს სკოლებში ჯანსაღი კვების პროგრამა.
                    დღეისათვის გაკვეთილებს უმეტესად მშიერი ბავშვები ესწრებიან. სახელმწიფო ვერ უზრუნველყოფს მოსწავლეთა კვებას. 
                    ბევრ ოჯახს არ აქვს შესაძლებლობა შვილს სახლიდან გაატანოს საკვები, რაც ზრდის ბავშვებს შორის უთანასწორობას. 
                    ბევრ სკოლაში არ არსებობს ბუფეტი. სადაც ბუფეტი ფუნქციონირებს, ეს იმის ხარჯზე, 
                    რომ სკოლის სივრცე ნაქირავები აქვს კერძო პირს და ბუფეტის ნაცვლად იქ გახსნილი აქვს მაღაზია, 
                    სადაც ჯანმრთელობისთვის ზიანის მომტანი პროდუქტებით ვაჭრობს. ე.წ ბუფეტში იყიდება გაზიანი სასმელები, მდარე, 
                    საეჭვო ხარისხის ტკბილეული და ცომეული, რაც ეწინააღმდეგება განათლებისა და მეცნიერების მინისტრის ბრძანება N410-ს, 
                    რომლითაც განსაზღვრულია სასკოლო კვების აკრძალული პროდუქტების ჩამონათვალი (საღეჭი რეზინი, კანფეტები, ჩიფსები, 
                    ჟელიბონი და ა.შ.)""",
    "short_description": "განათლების სამინისტრომ დაჩქარებული წესით დანერგოს ჯანსაღი სასკოლო კვების პროგრამა." 
                        "მუშაობის პროცესი გახადოს გამჭვირვალე და ჩაგვაყენოს საქმის კურსში, რას აპირებს სახელმწიფო ამ მიმართულებით.",
    "url_name": "jansagi-kveba",
    "img1": "https://healthyschoolscampaign.org/dev/wp-content/uploads/2020/01/Judging-Cooking-up-Change-2015-92_Blog.jpg",
    "img2": "https://www.pewtrusts.org/-/media/post-launch-images/2016/10/school_strategies_promote_healthy_eating/school_strategies_promote_healthy_eating_16x9.jpg",
    "img3": "https://againstallgrain.com/wp-content/uploads/2020/08/lunchbox-blog-scaled.jpg",
    "img4": "https://www.brookings.edu/wp-content/uploads/2017/05/rtr2jl3x.jpg",
    "img5": "https://familydoctor.org/wp-content/uploads/2011/01/35992525_l.jpg",
    },

    ]
}


if __name__ == "__main__":
    from routes import *
    app.run(debug=True)
