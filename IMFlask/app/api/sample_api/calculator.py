"""
Calculator API
"""
from flask_validation_extended import Validator, Query
from app.api import response, bad_request
from app.api.sample_api import sample_api as api
from app.api.decorator import timer
from controller import calculator


@api.route('/add')
@Validator(bad_request)
@timer
def add_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.add(a, b))


@api.route('/subtract')
@Validator(bad_request)
@timer
def subtract_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.subtract(a, b))


@api.route('/multiply')
@Validator(bad_request)
@timer
def multiply_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.multiply(a, b))


@api.route('/divide')
@Validator(bad_request)
@timer
def divide_api(
    a=Query(int),
    b=Query(int)
):
    return response(calculator.divide(a, b))