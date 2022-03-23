from django.urls import path
from . import views

urlpatterns = [


    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<int:pk>/<formulaire>/", views.blog_formulaire, name="blog_formulaire"),
    path("<int:pk>/<formulaire>/<thanks>/", views.blog_thanks, name="blog_thanks"),
    path("<int:pk>/<category>/", views.blog_category, name="blog_category"),
    path("<a_propos>/", views.blog_a_propos, name="blog_a_propos"),



]

