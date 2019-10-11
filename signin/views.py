from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ExtendedUserCreationForm, UserProfileForm,Editprofile

from django.contrib.auth.decorators import login_required


def index(request):

    if request.user.is_authenticated:
        username = request.user.username
        email= request.user.email
        first_name= request.user.first_name

        current_user=request.user
        obj=UserProfile.objects.get(user=current_user)
        flat_number=obj.flat_number
        mobile_number=obj.mobile_number

        
    else:
            username='not logged in'
            flat_number='unknown'
            email='unknown'
            mobile_number='unknown'
            first_name='unknown'


    context = {'username': username,'flat_number': flat_number,'mobile_number': mobile_number,'email':email,'first_name': first_name}

    return render(request, 'index.html', context)





def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')


    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm(request.POST)
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)



@login_required
def edit(request):
    
    
    
    if request.method == 'POST':
        
        form = Editprofile(request.POST,instance=request.user)
        if form.is_valid():
 
            form.save()
            print("valid")
            return redirect('index')
    else:
        
        form = Editprofile(instance=request.user)
    return render(request, 'edit.html', {
        'form': form
    })
