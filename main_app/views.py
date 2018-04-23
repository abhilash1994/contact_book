# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from models import Contact as Ct

# Create your views here.


class Contact(View):

    def get(self, request):
        print request.GET
        return HttpResponse('Hello world!')

    def post(self, request):
        return None

    def delete(self, request):
        return None

    def put(self, request):
        return None


class SearchName(View):

    def get(self, request):
        print "Received null"
