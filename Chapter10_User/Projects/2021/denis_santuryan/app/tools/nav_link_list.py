def generate_pages():
    """
    generates links and titles for navbar
    navbar either has an auth button or a button for the logged-in user
    automatically determines if the user is logged in
    returns a list of tuples with the following format: (page link, page title)
    """
    pages_nav_list = [
        ("posts.list_posts", "პოსტები"),
        ("profiles.list_people", "ხალხი"),
        ("list_pages", "გვერდები"),
        ("auth", "შესვლა")
    ]

    from flask_login import current_user
    if current_user.is_authenticated:
        pages_nav_list[3] = ('profiles.profile', current_user.username.upper())

    return pages_nav_list
