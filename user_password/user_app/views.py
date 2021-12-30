from django.shortcuts import render
from user_app.forms import UserForm,UserProfileInfoForm

# Need to import lot of built in tools for LOGIN & LOGOUT
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# views for basic index
def index(request):
    return render(request,'user_app/index.html')


@login_required()
def special(request):
    return HttpResponse("U are login, ThkU!")


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered=False

    if request.method == 'POST':
        #Then we are going to do get information from both of the forms
        user_form=UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # Now Check If Both Forms Are Valid

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            # can't commit yet bcz we still need to Manipulate
            profile = profile_form.save(commit=False)

            # Set ONE-TO-ONE Relationship b/w UserForm & UserProfileInfoForm

            profile.user = user

            if 'profile_pic' in request.FILES:

                profile.profile_pic=request.FILES['profile_pic']

             #Now Save Model
            profile.save()


            # Registeration Successful
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form= UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'user_app/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

# Create Views for User Login same as Registration views
def user_login(request):
    if request.method=='POST':
        ## FIRST GET USERNAME & PASSWORD
        username=request.POST.get('username')
        password=request.POST.get('password')

        ## User Authentication Authenticate username and password
        user= authenticate(username=username, password=password)

        # If we have a user

        if user:
            #Check it Account is Active
            if user.is_active:
                #log th user in
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("This Account Is Not Active!")

        else:

            print("Someone try to login and failed!")
            print("They are used username:{} ang password:{}".format(username, password))
            return HttpResponse("Invalid Login Details supplied.")

    else:
        return render(request, 'user_app/login.html', {})





