from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from .form import Registration, ProfileUpdate, UserUpdateForm
from django.contrib.auth.models import User
from app1.middleware import authenticated

@authenticated
def register(request):
    if request.method == 'POST':
        register_form = Registration(request.POST)
        if(register_form.is_valid()):
            register_form.save()
        return redirect('users:login')
    else:
        register_form = Registration()
    context = {'register':register_form}
    return render(request, 'users/register.html', context)

def profile(request):
    return render(request, 'users/profile.html')

def updateProfile(request, id):
    user_instance = get_object_or_404(User, id=id)
    profile_instance = user_instance.profile  # Related Profile

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user_instance)
        profile_form = ProfileUpdate(request.POST, request.FILES, instance=profile_instance)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('users:profile')  
    else:
        user_form = UserUpdateForm(instance=user_instance)
        profile_form = ProfileUpdate(instance=profile_instance)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/updateProfile.html', context)

def logouts(request):
    logout(request)
    return redirect('app1:index')
