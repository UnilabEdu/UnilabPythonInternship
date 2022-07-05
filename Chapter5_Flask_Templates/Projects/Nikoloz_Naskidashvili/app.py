from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/blog')
def blog():
	articles = [
		{
			"image": "https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg",
			"title": "sample blog title",
			"body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque blandit suscipit enim et volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam pretium nisl et est ullamcorper sagittis. Quisque vestibulum ac ante et dictum. Quisque mi sapien, facilisis sit amet magna nec, sollicitudin egestas arcu. Vivamus eu quam a velit aliquam interdum vel sed neque. Morbi a pharetra purus, ac eleifend lorem. Donec ac urna turpis. Nunc malesuada ipsum in mauris dignissim, at dapibus nibh tempus. Donec hendrerit ligula lorem, at bibendum est viverra sed.",
			"date": "22/07/2022"
		},
		{
			"image": "https://cdn.searchenginejournal.com/wp-content/uploads/2019/08/c573bf41-6a7c-4927-845c-4ca0260aad6b-1520x800.jpeg",
			"title": "sample blog title",
			"body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque blandit suscipit enim et volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam pretium nisl et est ullamcorper sagittis. Quisque vestibulum ac ante et dictum. Quisque mi sapien, facilisis sit amet magna nec, sollicitudin egestas arcu. Vivamus eu quam a velit aliquam interdum vel sed neque. Morbi a pharetra purus, ac eleifend lorem. Donec ac urna turpis. Nunc malesuada ipsum in mauris dignissim, at dapibus nibh tempus. Donec hendrerit ligula lorem, at bibendum est viverra sed.",
			"date": "14/05/2022"
		},
		{
			"image": "https://www.akamai.com/site/im-demo/perceptual-standard.jpg?imbypass=true",
			"title": "sample blog title",
			"body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque blandit suscipit enim et volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam pretium nisl et est ullamcorper sagittis. Quisque vestibulum ac ante et dictum. Quisque mi sapien, facilisis sit amet magna nec, sollicitudin egestas arcu. Vivamus eu quam a velit aliquam interdum vel sed neque. Morbi a pharetra purus, ac eleifend lorem. Donec ac urna turpis. Nunc malesuada ipsum in mauris dignissim, at dapibus nibh tempus. Donec hendrerit ligula lorem, at bibendum est viverra sed.",
			"date": "24/05/2022"
		}
	]

	return render_template("blog.html", articles=articles)


@app.route('/sign-up')
def sign_up():
	return render_template("signup.html")


if __name__ == '__main__':
	app.run()
