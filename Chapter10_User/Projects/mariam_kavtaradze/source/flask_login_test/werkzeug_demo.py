from werkzeug.security import generate_password_hash, check_password_hash

password = "random_password"

hashed_pass_in_db = generate_password_hash(password)

if __name__ == '__main__':
    print(hashed_pass_in_db)

    login_password = "new_pass"

    result = check_password_hash(hashed_pass_in_db, login_password)
    if result:
        print("login successfuul")
    else:
        print("inorrect pass")
