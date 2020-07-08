from django.urls import path
from articlesApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articlesApp'
urlpatterns = [
    path("home", views.main, name="home"),
    path("main", views.main, name="main"),
    path("add-category", views.category, name="add-category"),
    path("add-article", views.article, name="add-article"),
    path("", views.feed, name="feed"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name="profile"),
    path("contact", views.contact, name="contact"),
    path("posts/<int:num>" , views.post, name="post"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

