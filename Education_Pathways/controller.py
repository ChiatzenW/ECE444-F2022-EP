# this is the controller

from flask import jsonify, request
from flask_restful import Resource, reqparse
# from flask_cors import cross_origin
from config import app
from model import *
from fuzzy import nysiis
import re


# -------------------- Course related --------------------
class SearchCourse(Resource):
    def get(self):
        input = request.args.get('input')
        code = re.findall('[a-zA-Z]{3}\d{3}[hH]?\d?', input)
        if code:
            code = code[0].upper()
            if len(code) == 6:
                code += 'H1'
            elif len(code) == 5:
                code += '1'
            if Course.objects(code=code):
                try:
                    resp = jsonify({'course': Course.get(code)})
                    print(Course.get(code))
                    resp.status_code = 200
                    return resp
                except Exception as e:
                    resp = jsonify({'error': 'something went wrong'})
                    resp.status_code = 400
                    return resp
        input = ' '.join([nysiis(w) for w in input.split()])
        try:
            search = Course.objects.search_text(input).order_by('$text_score')
            resp = jsonify(search)
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('input', required=True)
        data = parser.parse_args()
        input = data['input']
        code = re.findall('[a-zA-Z]{3}\d{3}[hH]?\d?', input)
        if code:
            code = code[0].upper()
            if len(code) == 6:
                code += 'H1'
            elif len(code) == 5:
                code += '1'
            if Course.objects(code=code):
                try:
                    resp = jsonify({'course': Course.get(code)})
                    resp.status_code = 200
                    return resp
                except Exception as e:
                    resp = jsonify({'error': 'something went wrong'})
                    resp.status_code = 400
                    return resp
        input = ' '.join([nysiis(w) for w in input.split()])
        try:
            search = Course.objects.search_text(input).order_by('$text_score')
            resp = jsonify(search)
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp


class ShowCourse(Resource):
    def get(self):
        code = request.args.get('code')
        if not Course.objects(code=code):
            resp = jsonify({'message': f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp
        try:
            resp = jsonify({'course': Course.get(code)})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', required=True)
        data = parser.parse_args()
        code = data['code']
        if not Course.objects(code=code):
            resp = jsonify({'message': f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp
        try:
            resp = jsonify({'course': Course.get(code)})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp
