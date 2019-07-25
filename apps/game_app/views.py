from django.shortcuts import render,redirect
from django.contrib import messages
from apps.breath_app.models import User


from django.shortcuts import render, redirect

# Create your views here.
def Dashboard(request):
    pass
    return render(request, "game_app/dashboard.html") 

def ProcessWelcome(request):
    pass
    #code that takes info from welcome form and puts journal entry into database
    #takes action from button 'Start Game' and sends you to taste page
    return redirect('/serenity_now/taste')

def Taste(request):
    pass
    #page that has drop down menu for choosing your taste 
    #earn points as well 
    return render(request,'game_app/taste.html')

def ProcessTaste(request):
    pass
    #code that takes info from form on taste.html and enters it into database
    return redirect('/serenity_now/success')

def Shift(request):
    pass
    #code to display on shift.html
    return render(request, 'game_app/shift.html')

def ProcessShift(request):
    gratitudeList = request.POST["gratitudeList"]
    #code to add gratitude list to the database
    return redirect('/serenity_now/taste')

def Success(request):
    pass
    return render(request,'game_app/success.html')

def ProcessSuccess(request):
    pass
    return redirect('/serenity_now/taste')

def SerenityStay(request):
    pass
    return render(request,'game_app/serenity.html')

def ProcessSerenityStay(request):
    pass
    return redirect('/serenity_now/serenityStay')

def Touch(request):
    pass
    return render(request,'game_app/touch.html')

def ProcessTouch(request):
    pass
    return redirect('/serenity_now/success')

# def OurLogic(request):
#     my_user = User.objects.get(request.session["user_id"])
#     if my_user.taste != 0:
#         return redirect('/serenity_now/touch')
#     else: 
#         return redirect('serenity_now/taste')

#     if my_user.touch != 0:
#         return redirect('/serenity_now/visual')
#     elif my_user.visual != 0:
#         return redirect('/serenity_now/auditory')
#     elif my_user.auditory !=0:
#         return redirect('/serenity_now/serenityStay')
#     else:
#         return redirect('/serenity_now/serenityStay')

def Visual(request):
    pass
    return redirect("/serenity_now/success")

def ProcessVisual(request):
    pass
    return redirect("/serenity_now/success")


