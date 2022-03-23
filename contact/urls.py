from django.urls import path
from . import views


urlpatterns = [

    path('', views.blog_comment, name='contact'),
    path("<services>/", views.blog_services, name="blog_services"),
]