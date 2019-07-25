from django.conf.urls import url
from . import views

# Login and Registration
urlpatterns = [
    url(r'^$', views.Index),
    url(r'^registration$', views.Registration),
    url(r'^login$', views.Login),
    url(r'^logout$', views.Logout),


    # Render Templates
    # url(r'^serenity$', views.Serenity),
]
