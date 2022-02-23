# app.py

from api import API
from middleware import Middleware

app = API()

# function based handlers

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

@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template(
        "index.html",
        context={"name": "Bumbo", "title": "Best Framework"}
    )

@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}

@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text"

@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")

# class-based handlers

@app.route("/book")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Books Page"
    
    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

# Django-like handlers

def handler(req, resp):
    resp.text = "sample"

app.add_route("/sample", handler)

# exception handler

def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)

app.add_exception_handler(custom_exception_handler)


# custom middleware

class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)
    
    def process_response(self, req, res):
        print("Processing response", req.url)

app.add_middleware(SimpleCustomMiddleware)
