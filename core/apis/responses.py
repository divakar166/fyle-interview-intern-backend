from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))
    
    @classmethod
    def respond_error(cls, message, status_code, error_type='FyleError'):
        response = {
            "error": error_type,
            "message": message,
        }
        return make_response(jsonify(response), status_code)