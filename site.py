# add web.py
import web

# list all of the URLs for the server
urls = (
	'/', 'index'
)

# prepare to render template files
render = web.template.render("templates/")

# homepage
class index:
	# GET /
	def GET(self):
		return render.index()

# this starts the server if you've called "python site.py"
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
