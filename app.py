# app.py

from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the home page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the about page"
