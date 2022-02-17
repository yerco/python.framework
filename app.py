# app.py

from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the home page"

# @app.route("/home")
# def home2(request, response):
#     response.text = "Hello from the SECOND HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the about page"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello {name}"

@app.route("/tell/{age:d}")
def tell_age(request, response, age):
    response.text = f"Age is {age}"

@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"

@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"
    
    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

def handler(req, resp):
    resp.text = "sample"

app.add_route("/sample", handler)
