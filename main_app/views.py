# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from models import Contact as Ct

# Create your views here.


class Contact(APIView):
    def post(self, request):
        return None

    def delete(self, request):
        return None

    def put(self, request):
        return None


class SearchName(APIView):

    def get(self, request):
        if request.user.is_authenticated():
            print "Hello, user is authenticated"
        # names = [contact.name for contact in Ct.objects.all()]
        return Response("names")


class SearchEmail(APIView):
    def get(self, request):
        emails = [contact.email for contact in Ct.objects.all()]
        return Response(emails)


@method_decorator(csrf_exempt, name='post')
class Login(APIView):
    def post(self, request):
        print request.data
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email)
        print user
        if user:
            user = authenticate(username=user[0], password=password)
        print user
        if user:
            login(request, user)
            token, created_flag = Token.objects.get_or_create(user=user)
            response = Response('Logged in! :O')
            response['Authorization'] = token
        else:
            return Response("Invalid User")
        return response


@method_decorator(csrf_exempt, name='post')
class Signup(APIView):

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            print request.user
            request.user = user
            # request.session.user = user
            # return HttpResponseRedirect('/')
            return HttpResponse('Somewhere here in the signup flow')
        print request.user
        return HttpResponse('Logged in! :O')


@method_decorator(csrf_exempt, name='post')
class Logout(APIView):

    def post(self, request):
        print request.user
        request.user.auth_token.delete()
        logout(request)
        return Response("Logged out")
