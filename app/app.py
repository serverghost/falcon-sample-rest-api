import falcon
import socket
import json

class GreetingsResource:
    def on_get(self, req, resp):
        host_name = socket.gethostname()
        response = {
            "message": "Hello World from " + host_name
        }

        resp.media = response

class SquareResource:
    def on_get(self, req, resp):
        response = {
            "message": "Send a POST method with number and it will return the square of it."
        }

        resp.media = response

    def on_post(self, req, resp):
        print(req.media["number"])
        number_data = req.media["number"]
        square_data = number_data * number_data
        response = {
            "number": number_data,
            "square": square_data
        }

        resp.media = response

api = falcon.API()
#api.req_options.auto_parse_form_urlencoded=True
api.add_route('/greetings', GreetingsResource())
api.add_route('/square', SquareResource())