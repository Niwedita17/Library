from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='home'),
    url(r'^book/$', views.view_books, name='view_books'),
    url(r'^book/add/$', views.add_book, name='add_book'),
    url(r'^borrower/$', views.view_borrower, name='view_borrower'),
    url(r'^borrower/add/$', views.add_borrower, name='add_borrower'),
    url(r'^employer/$', views.view_employer, name='view_employer'),
    url(r'^employer/add/$', views.add_employer, name='add_employer'),
    #url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^issue/$', views.view_issue, name='view_issue'),
    url(r'^issue/new/$', views.new_issue, name='new_issue'),
    url(r'^return_book/$', views.return_book, name='return_book'),
    #url(r'^delete_book/$', views.ViewDeletePost, name='delete_book'),
    #url(r'^update_book/$', views.ViewUpdatePost.as_view(), name='update_book'),
    #url(r'^book/search/$', views.search_books, name='search_books'),
]
