"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from libman import views as core_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.redir, name='redirect_view'),
    url(r'^student_login/$', core_views.student_login, name='student_login'),
    url(r'^librarian_login/$', core_views.librarian_login, name='librarian_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/library'}, name='logout'),
    url(r'^student_signup/$', core_views.student_signup, name='student_signup'),
    url(r'^librarian_signup/$', core_views.librarian_signup, name='librarian_signup'),
    url(r'^library/', include('libman.urls')),
]
