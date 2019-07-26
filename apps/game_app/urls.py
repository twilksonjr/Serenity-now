from django.conf.urls import url
from . import views

# Game App URLS
urlpatterns = [

#Render Routes
#last route is Dashboard_the Welcome Page for the Game App
    url(r'^taste$', views.Taste),
    url(r'^shift$', views.Shift),
    url(r'^success$', views.Success),
    url(r'^serenityStay$', views.SerenityStay),
    # url(r'^touch$', views.Touch),
    url(r'^visual$', views.Visual),
    # url(r'^auditory$', views.Auditory),
    # url(r'^smell$', views.Smell),


   


#Redirect or Hidden Process Routes

    url(r'^processWelcome$', views.ProcessWelcome),
    url(r'^processTaste$', views.ProcessTaste),
    url(r'^processShift$', views.ProcessShift),
    url(r'^processSuccess$', views.ProcessSuccess),
    # url(r'^processTouch$', views.ProcessTouch),
    url(r'^processVisual$', views.ProcessVisual),
    # url(r'^processAuditory$', views.ProcessAuditory),
    # url(r'^processSmell$', views.ProcessSmell),
    url(r'^processSerenityStay$', views.ProcessSerenityStay),

    url(r'^processOurLogic$', views.ProcessOurLogic),

    
     
   
     url(r'^$', views.Dashboard),
  


    
]
