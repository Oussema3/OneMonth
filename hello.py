from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
	title="Home Page"
	return render_template("index.html", title=title)

@app.route("/about")
def about():
	title="About Page"
	return render_template("about.html", title=title)

@app.route("/contact")
def contact():
	title="Contact Page"
	return render_template("contact.html", title=title)









if __name__=="_main_":
    app.run(debug=True) 
