from flask import Flask
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
password = "BestPass"


if __name__ == '__main__':
        hashed = bcrypt.generate_password_hash(password=password)

        print(f"{hashed}")

