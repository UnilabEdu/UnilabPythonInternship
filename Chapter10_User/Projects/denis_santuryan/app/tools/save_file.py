def save_file(username, file, folder):
    """
    saves a file with a name completely safe from accidental overwriting
    saves to a folder in app/static/uploads
    example folder names: 'post_uploads', 'profile_pictures'
    """

    from werkzeug.utils import secure_filename
    from random import randint

    title = secure_filename(f'{username}_{randint(10000000,99999999)}_{file.filename}')
    file.save(f'app/static/uploads/{folder}/{title}')

    return title
