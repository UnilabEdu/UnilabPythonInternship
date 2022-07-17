from werkzeug.security import check_password_hash, generate_password_hash

hashed_pass = generate_password_hash('bestkeptsecret')

if __name__ == "__main__":
    print(hashed_pass)

    check = check_password_hash(hashed_pass, 'bestkeptsecret')
    print(f'Result: {check}')