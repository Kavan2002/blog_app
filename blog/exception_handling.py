from django.core.exceptions import FieldError
from django.http import response
from django.shortcuts import redirect


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, Exception):
        print('exception_middleware ===', FieldError(Exception))
        return redirect('/')
