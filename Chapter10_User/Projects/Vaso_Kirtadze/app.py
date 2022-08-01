from werkzeug.security import check_password_hash, generate_password_hash

hased_pass = generate_password_hash("bestsekret")


if __name__ == '__main__':
    print(hased_pass)

    check = check_password_hash(hased_pass, "bestsekret")
    print(f'{check}')


