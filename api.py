# api.py

from webob import Request, Response

class API:
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = Response()
        response.text = "Hola Mundo"

        return response(environ, start_response)

