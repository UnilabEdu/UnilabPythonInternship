from flask import Flask, render_template

server = Flask(__name__)

products = {
    "apple":{
        "1":{
            "id": "1",
            "model": "Apple iPhone 13 128GB Blue",
            "price": "1999 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/238/123479_1.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/238/123479_5.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/238/123479_3.jpg.jpg"
                      ),
            "info": {
                    "screen":        "6.1",
                    "discernment":   "1170 x 2532",
                    "Material used": "Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame",
                    "Model/PN":      "MLPK3RM/A"
                    }
            },
        "2":{
            "id": "2",
            "model": "Apple iPhone 15 Pro Max 256GB - Black Titanium",
            "price": "4399 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/300/iPhone_15_Pro_Max_Black_Titanium_PDP_Image_Position-1_alt__ww-EN.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/300/iPhone_15_Pro_Max_Black_Titanium_PDP_Image_Position-2__ww-EN.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/300/iPhone_15_Pro_Max_Black_Titanium_PDP_Image_Position-4__ww-EN.jpg.jpg"
                      ),
            "info": {
                    "screen":        "6.7",
                    "discernment":   "1290 x 2796",
                    "Material used": "Glass front (Corning-made glass), glass back (Corning-made glass), titanium frame (grade 5)",
                    "Model/PN":      "A3106 - MU773HX/A"
                    }
            },
        "3":{
            "id": "3",
            "model": "Apple iPhone 14 128GB Blue (Model A2882)",
            "price": "2399 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/259/WWEN_iPhone14_Q422_Blue_PDP_Image_Position-1a.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/259/WWEN_iPhone14_Q422_Blue_PDP_Image_Position-1b.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/259/WWEN_iPhone14_Q422_Blue_PDP_Image_Position-3.jpg.jpg"
                      ),
            "info": {
                    "screen":        "6.1",
                    "discernment":   "1170 x 2532",
                    "Material used": "Glass front (Gorilla Glass), glass back (Gorilla Glass), aluminum frame",
                    "Model/PN":      "A2882 - MPVN3HX/A"
                    }
            }
    },

    "samsung":{
        "1":{
            "id": "4",
            "model": "Samsung A546E Galaxy A54 (8GB/256GB) Dual Sim LTE/5G - Black",
            "price": "879 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/279/11_ga4j-yu.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/279/1_gb37-uq.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/279/11_ga4j-yu.png.jpg"
                      ),
            "info": {
                    "screen":        "6.4",
                    "discernment":   "1080 x 2400",
                    "Material used": "Glass front (Gorilla Glass 5), plastic frame, plastic back",
                    "Model/PN":      "SM-A546EZKDCAU"
                    }
            },
        "2":{
            "id": "5",
            "model": "Samsung S928B Galaxy S24 Ultra (12GB/256GB) LTE/5G Dual Sim - Gray",
            "price": "3649 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/314/148689_1_61gq-cr.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/314/148689_3_83vj-06.jpg.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/314/148689_5_79tt-th.jpg.jpg"
                      ),
            "info": {
                    "screen":        "6.8",
                    "discernment":   "1440 x 3088",
                    "Material used": "Glass front (Gorilla Glass Armor), glass back (Gorilla Glass), titanium frame)",
                    "Model/PN":      "SM-S928BZTGCAU"
                    }
            },
        "3":{
            "id": "6",
            "model": "Samsung A546E Galaxy A54 (6GB/128GB) Dual Sim LTE/5G - Green",
            "price": "779 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/279/2_hd9w-qh.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/279/1_c84d-hj.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/279/2_hd9w-qh.png.jpg"
                      ),
            "info": {
                    "screen":        "6.4",
                    "discernment":   "1080 x 2400",
                    "Material used": "Glass front (Gorilla Glass 5), plastic frame, plastic back",
                    "Model/PN":      "SM-A546ELGACAU"
                    }
            }
    },
    "google-pixel":{
        "1":{
            "id": "7",
            "model": "Google Pixel 8 Pro 5G (12GB/128GB) - Obsidian",
            "price": "2659 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/318/150446-1.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/318/150446-2.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/318/150446-3.png.jpg"
                      ),
            "info": {
                    "screen":        "6.7",
                    "discernment":   "1344 x 2992",
                    "Material used": "Glass front (Gorilla Glass Victus 2), glass back (Gorilla Glass Victus 2), aluminum frame",
                    "Model/PN":      "Pixel 8 Pro"
                    }
            },
        "2":{
            "id": "8",
            "model": "Google Pixel 6 Pro 5G (12GB/128GB) - Black",
            "price": "1449 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/318/150448-1.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/318/150448-2.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/318/150448-4.png.jpg"
                      ),
            "info": {
                    "screen":        "6.7",
                    "discernment":   "1440 x 3120",
                    "Material used": "Glass front (Gorilla Glass Victus), glass back (Gorilla Glass Victus), aluminum frame",
                    "Model/PN":      "Pixel 6 Pro"
                    }
            },
        "3":{
            "id": "9",
            "model": "Google Pixel 8 Pro 5G (12GB/256GB) - Porcelain",
            "price": "2899 ₾",
            "images":("https://alta.ge/images/thumbnails/900/650/detailed/323/151720__1_.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/323/151720__2_.png.jpg",
                      "https://alta.ge/images/thumbnails/900/650/detailed/323/151720__4_.png.jpg"
                      ),
            "info": {
                    "screen":        "6.7",
                    "discernment":   "1344 x 2992",
                    "Material used": "Glass front (Gorilla Glass Victus 2), glass back (Gorilla Glass Victus 2), aluminum frame",
                    "Model/PN":      "Pixel 8 Pro"
                    }
            }
    }

}


@server.route("/")
def home():
    for modelkey, modelname in products.items():
        for id, product in modelname.items():
    
            print(product["id"])
    return render_template("home.html",products=products)

@server.route("/login")
def login():
    return render_template("login.html")

@server.route("/signin/<id>")
def signin(id):

    return render_template("signin.html",id=id)

@server.route("/details/<id>")
def details(id):

    return render_template("details.html",id=id)


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=8080)