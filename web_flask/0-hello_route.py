from web_flask import app


@app.route("/airbnb-onepage", strict_slashes=False)
def hello():
	"""Return hello HBNB!"""
	return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
