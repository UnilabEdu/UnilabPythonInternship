from jinja2 import Template

#index.html > element


# a = "<href='{{url}}'>{{page_title}}</a>"
a = "<href='{{url}}'>{{page_title}}</a>"

template = Template(a)
url = "mysite.com"
page_title = "my site"

result = Template.render(url=url, page_title=page_title)
