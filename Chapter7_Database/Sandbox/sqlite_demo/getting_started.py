import sqlite3

dummy_data = [
    (1, "ხვალინდელი ამბავი", "ხვალ თბილისში საინტერესო ამბავი მოხდება"),
    (2, "უსახელო", "ზეგ თბილისში საინტერესო ამბავი მოხდება")
]


def select_all():
    return all


def select_by_id(record_id):
    return item

# create redirect to select_all
def create_item(args):
    return status

# update
def update_item(record_id, column_name, column_value):
    return status


def delet_item(record_id):
    return status


if __name__ == '__main__':
    # ვხსნი კავშირს ბაზასთან
    connection = sqlite3.connect("my_first.db")
    # კავშირიდან ამომაქვს კურსორი
    cursor = connection.cursor()

    # ვუშვებ კურსორით ბრძანებას
    cursor.execute("CREATE TABLE IF NOT EXISTS post (_id int, title text, description text)")

    # Create - ცხრილში მონაცემის ჩაწერა
    # cursor.execute("INSERT INTO post VALUES (0, 'დღევანდელი ამბავი', 'დღეს თბილისში საინტერესო ამბავი მოხდა')")
    cursor.execute("INSERT INTO post VALUES (?, ?, ?)",
                   (0, 'დღევანდელი ამბავი', 'დღეს თბილისში საინტერესო ამბავი მოხდა'))

    cursor.executemany("INSERT INTO post VALUES (?, ?, ?)", dummy_data)

    # Read - ცხრილიდან მონაცემის წაკითხვა
    posts = cursor.execute("SELECT * FROM post").fetchall()  # ყველა ჩანაწერის წამოღება
    print(posts)
    posts = cursor.execute("SELECT * FROM post").fetchone()  # პირველი ჩანაწერის წამოღება
    print(posts)
    # ფილტრაცია და სორტირება
    posts = cursor.execute("SELECT * FROM post WHERE title IS NULL ORDER BY _id DESC ").fetchall()
    print(posts)

    # Update - ცხრილში მონაცემის განახლება
    cursor.execute("UPDATE post SET title = 'უსახელო' WHERE title IS NULL")

    # Delete - მონაცემის ცხრილიდან ამოშლა
    cursor.execute("DELETE FROM post WHERE _id IS 3")

    # იმ შემთხვევაში თუ ბრძანება ცვლის ცხრილს, ავსახავ ცვლილებას
    connection.commit()
    # ვხურავ კავშირს
    connection.close()
