from django.shortcuts import render,redirect
from django.contrib import messages
from apps.breath_app.models import User
from apps.game_app.models import SerenityShift

from django.shortcuts import render, redirect

# Create your views here.
def Dashboard(request):
    this_user_id = request.session["user_id"]
    this_user = User.objects.get(id=this_user_id) 
    name = this_user.first_name
    last_name = this_user.last_name
    context={
        "template_name": name,
        "template_lastname": last_name
    }

    return render(request, "game_app/dashboard.html", context) 

def ProcessWelcome(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id) 

    journal = request.POST["journal"]

    sBegin = request.POST["range"]
    # suds_level_end
    # player = models.ForeignKey(User, related_name="list_of_shifts_associated_with_user", default = "")
    # currency = models.IntegerField(default=0)
    # taste = models.IntegerField(default=0)
    # touch = models.IntegerField(default=0)
    # visual = models.IntegerField(default=0)
    # auditory = models.IntegerField(default=0)
    # smell = models.IntegerField(default=0)
    # num_breathing = models.IntegerField(default=0)
    # gratitude_list = models.TextField(default = "")
    # activity_list = models.TextField(default = "")
    # observations = models.TextField(default = "")
    # pass
    this_user_shift = SerenityShift.objects.create(suds_level_begin=sBegin, player=this_user,journal=journal)

    #code that takes info from welcome form and puts journal entry into database
    #takes action from button 'Start Game' and sends you to taste page
    return redirect('/serenity_now/taste')

def Taste(request):
    pass
    #page that has drop down menu for choosing your taste 
    #earn points as well 
    return render(request,'game_app/taste.html')

def ProcessTaste(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    this_shift_id = this_shift.id
    my_shift = SerenityShift.objects.get(id=this_shift_id)
    my_shift.taste = request.POST["taste"]
    my_shift.save()
    # for shift in this_shift:
    # taste=request.POST["taste"]


    #code that takes info from form on taste.html and enters it into database
    return redirect('/serenity_now/success')

def Shift(request):
#code to display on shift.html

    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id) 
    name_first = this_user.first_name
    name_last = this_user.last_name 
    context={
        "name_template_first": name_first,
        "name_template_last": name_last,

    } 
    return render(request, 'game_app/shift.html', context)

def ProcessShift(request):
    print("are you in the PROCESS SHIFT FUNCTION: YES!!!!!")
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    this_shift_id = this_shift.id
    my_shift = SerenityShift.objects.get(id=this_shift_id)
    my_shift.gratitude_list = request.POST["gratitudeList"]
    print("Grab from post the gratitude list***************************")
    print(request.POST["gratitudeList"])
    my_shift.activity_list = request.POST["activityList"]
    my_shift.save()   
    #code to add gratitude list to the database
    return redirect('/serenity_now/processOurLogic')

def Success(request):
    this_user_id = request.session["user_id"]
    this_user = User.objects.get(id=this_user_id) 
    name = this_user.first_name
    last_name = this_user.last_name
    context={
        "template_name": name,
        "template_lastname": last_name
    }    
    return render(request,'game_app/success.html', context)

def ProcessSuccess(request):
    pass
    return redirect('/serenity_now/processOurLogic')

def SerenityStay(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    name=this_user.first_name
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    this_shift_id = this_shift.id
    my_shift = SerenityShift.objects.get(id=this_shift_id)
    # my_shift.suds_level_end = request.POST["end_range"]
    # my_shift.save()
    grat_list = my_shift.gratitude_list
    act_list = my_shift.activity_list 
    journal = my_shift.journal
    begin_stress = my_shift.suds_level_begin   
    end_stress = my_shift.suds_level_end
    breath_count = my_shift.num_breathing
    context={
        "name":name,
        "begin_stress": begin_stress,
        "end_stress": end_stress,
        "breath_count": breath_count,
        "grat_list": grat_list,
        "act_list": act_list,
        "journal": journal,
        }  
    
    return render(request,'game_app/serenity.html', context)

def ProcessSerenityStay(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    name=this_user.first_name
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    this_shift_id = this_shift.id
    my_shift = SerenityShift.objects.get(id=this_shift_id)
    my_shift.suds_level_end = request.POST["end_range"]
    my_shift.save()

    # grat_list = my_shift.gratitudeList
    # act_list = my_shift.activityList 
    # journal = my_shift.journal
    # begin_stress = my_shift.suds_level_begin   
    # end_stress = my_shift.suds_level_end
    # context={
    #     "name":name,
    #     "begin_stress": begin_stress,
    #     "end_stress": end_stress,
    #     "breath_count": breath_count,
    #     "grat_list": grat_list,
    #     "act_list": act_list,
    #     "journal": journal,
    #     }  
    
    return redirect('/serenity_now/serenityStay')

# def Touch(request):
#     pass
#     return render(request,'game_app/touch.html')

# def ProcessTouch(request):
#     pass
#     return redirect('/serenity_now/success')

def ProcessOurLogic(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    # for shift in this_shift:
    

# if user has answered question go on to next question in the list 
# set a boolean? and then at end loop thorugh those to check? 
    
    if this_shift.visual != 0:
        print("inside this_shift.visual")
        print(this_shift.visual)
        return render (request, 'game_app/serenity.html')
    
    if this_shift.taste != 0:
        return redirect ('/serenity_now/visual')
    # elif this_shift == 0: 
    #     return redirect('serenity_now/taste')

    
    # else:
    #   return redirect('/serenity_now/visual')

    # if this_shift.visual != 0 :
    #     return redirect('serenity_now/auditory')
    # else: 
    #     return redirect('serenity_now/visual')
      
    # if this_shift.auditory != 0:
    #     return redirect('serenity_now/smell')
    # else:
    #     return redirect('serenity_now/auditory')

    # if this_shift.smell != 0:
    #     return redirect('serenity_now/shift')
    # else:
    #     return redirect('serenity_now/smell')
          
    # if this_shift.num_breathing !=0:
    #     return redirect('serenity_now/serenityStay')
    # else:
    #     return redirect('serenity_now/shift')


def Visual(request):
    pass
    return render(request, 'game_app/visual.html')


def ProcessVisual(request):
    my_user_id = request.session["user_id"]
    this_user = User.objects.get(id=my_user_id)
    # this_shift = SerenityShift.objects.filter(player=this_user)
    this_shift = SerenityShift.objects.last()
    this_shift_id = this_shift.id
    my_shift = SerenityShift.objects.get(id=this_shift_id)
    # print("subs from visual html capture**********")
    # print(request.POST["subs"])
    my_shift.visual = request.POST["subs"]
    my_shift.save()
    return redirect("/serenity_now/success")

# def Auditory(request):
#     pass
#     return render(request, 'game_app/auditory.html')

# def ProcessAuditory(request):
#     pass
#     return redirect("/serenity_now/success")
# def Smell(request):
#     pass
#     return render(request, 'game_app/smell.html')

# def ProcessSmell(request):
#     pass
#     return redirect("/serenity_now/success")