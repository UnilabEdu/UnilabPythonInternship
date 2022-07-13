from jinja2 import Template

# index.html > elemnt


# a = f"<a href='{url}'>{page_title}</a>"

a = "<a href='{{url}}'>{{page_title}}</a>"
template = Template(a)

url = "mysite.ge"
page_title = "ჩემი საიტი"

result = template.render(url="avoe.ge", page_title="გადმოწერე რაც გინდა")
print(result)