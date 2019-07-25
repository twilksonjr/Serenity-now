from django.conf.urls import url
from . import views

# Serenity Store URLS
urlpatterns = [
    url(r'^$', views.Index),

]
