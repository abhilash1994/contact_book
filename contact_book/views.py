from django.http import HttpResponse
from django.views import View


class Contact(View):

    def get(self, request):
        return HttpResponse('Hello world!')

    def post(self, request):
        return None

    def delete(self, request):
        return None

    def put(self, request):
        return None
