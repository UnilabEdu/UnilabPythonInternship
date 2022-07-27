from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "random_password"

if __name__ == "__main__":
    hashed_pass_in_db = bcrypt.generate_password_hash(password=password)
    print(f'Hashed_Pass: {hashed_pass_in_db}')

    login_password = "new_pass"

    result = bcrypt.check_password_hash(hashed_pass_in_db, login_password)
    if result:
        print("login successfuul")
    else:
        print("inorrect pass")
