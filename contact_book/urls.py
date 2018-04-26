"""contact_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_swagger.views import get_swagger_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.documentation import include_docs_urls
from main_app.views import Contact, Login, Logout, SearchName, SearchEmail, Signup

schema_view = get_swagger_view(
    title='Contact Book API'
)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^contact', Contact.as_view(), name='home'),
    url(r'^$', schema_view),
    url(r'^name/', SearchName.as_view(), name='home'),
    url(r'^email/', SearchEmail.as_view(), name='home'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^register/$', csrf_exempt(Signup.as_view())),
    url(r'^login/$', csrf_exempt(Login.as_view())),
    url(r'^logout/$', csrf_exempt(Logout.as_view())),
    url(r'^docs/', include_docs_urls(title='Contact Book'))
]
