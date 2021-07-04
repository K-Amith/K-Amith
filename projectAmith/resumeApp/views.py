from django.shortcuts import render
from . import forms
from resumeApp.models import MyObjective,MyProfile,Skill,Feed_back,Project,PersonalDetail,Hobbie,Workshop,Award

# Create your views here.

def index(request):


    form = forms.Feedback_form(request.POST  or None)
    url_position=""
    if request.method == 'POST':


        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            feedbacks = form.cleaned_data['Feedback']
            fb = Feed_back(name=name,email_id=email,feed_back =feedbacks)
            fb.save()
            url_position="#section9"


    skills_list =Skill.objects.order_by('s_id')
    feed_backs_list =Feed_back.objects.order_by('f_id')
    projects_list =Project.objects.order_by('p_id')
    pd_lists =PersonalDetail.objects.order_by('pd_id')
    hobbies_list =Hobbie.objects.order_by('h_id')
    workshop_list =Workshop.objects.order_by('w_id')
    awards_list =Award.objects.order_by('a_id')
    objective_list =MyObjective.objects.order_by('obj_id')
    profile_list =MyProfile.objects.order_by('mp_id')


    my_dict ={'profile':profile_list,'objective':objective_list,'skilles':skills_list,'feed_backs':feed_backs_list,'projects':projects_list, 'hobbies':hobbies_list,'workshops':workshop_list,'awards':awards_list,'personals':pd_lists,'form':form}


    return render(request,'resumeApp/index.html',context=my_dict)
