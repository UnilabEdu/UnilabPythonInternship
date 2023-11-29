from os import path
from string import ascii_lowercase


class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = "flaskappkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "models", "instance" ,"database.db")
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "assets")
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
    