from jinja2 import Template
from ftfy import fix_encoding

template_pair = """</br>
<b>Მომხმარებლის კითხვა:</b> {{ question }}!
</br>
<b>Ბოტის პასუხი:</b> {{ answer }}!
</br>
_______________________
</br>"""


def generate_pair(answer, question):
    t = Template(template_pair)
    result = t.render(
        question=question,
        answer=answer
    )

    return result


def write_to_html(text):
    file = open("qna.html", "a", encoding='utf-8')
    file.write(text)
    file.close()


def process_csv():
    with open('Estories.csv', mode='r', encoding='utf-8') as csv_file:
        next(csv_file)
        for line in csv_file:
            if len(fix_encoding(line).split('",')) == 2:
                pair = fix_encoding(line).split('",')
                question = pair[0]
                answer = pair[1]
            else:
                pair = fix_encoding(line).split(',')
                question = pair[0]
                answer = pair[1]
            question = question[1:]
            qna_pair = generate_pair(question, answer)
            write_to_html(qna_pair)

            # question = question[1:]
            # print(f"{answer=}\n{question=}\n")

    #
    # list_lines = (s.rstrip().split(",") for s in pairs)
    #
    # columns = next(list_lines)  # first line of the list
    #
    # print(columns)


if __name__ == '__main__':
    process_csv()
