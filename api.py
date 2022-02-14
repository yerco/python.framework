# api.py

from webob import Request, Response

class API:
    def __init__(self) -> None:
        self.routes = {}
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def handle_request(self, request):
        user_agent= request.environ.get("HTTP_USER_AGENT", "No user agent found.")

        response = Response()
        response.text = f"Hola, my friend with this user agent: {user_agent}"

        return response
