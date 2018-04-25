# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import ContactBookSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from models import Contact as Ct

# Create your views here.


class Contact(APIView):
    """
    post:
    Create a new contact instance.

    delete:
    Delete an existing contact instance

    put:
    Update an exisiting contact instance
    """
    def post(self, request, format=None):
        if request.user.is_authenticated():
            serializer = ContactBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        if request.user.is_authenticated():
            email = request.data['email']
            Ct.objects.filter(email=email).delete()
            return Response("Record deleted successfully", status=status.HTTP_200_OK)
        else:
            return Response({"Error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        return None


class SearchName(APIView):
    """
    Returns a list of contacts whose names are being searched for.
    """
    def get(self, request):
        if request.user.is_authenticated():
            name = request.data['name']
            names = [contact for contact in Ct.objects.filter(name=name)]
            return Response(names)
        else:
            return Response({"Error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED)


class SearchEmail(APIView):
    """
    Returns a list of contact whose emails are being searched for.
    """
    def get(self, request):
        if request.user.is_authenticated():
            email = request.data['email']
            emails = [contact for contact in Ct.objects.filter(name=email)]
            return Response(emails)
        else:
            return Response({"Error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED)


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
