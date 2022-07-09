from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username}")
            return redirect('login')
        else:
            password = form.cleaned_data.get('username')
            messages.error(request, f"{password}")

    else:
        form = UserRegisterForm()

        return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        update_user_form = UserUpdateForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)

        # print(update_profile_form.data)
        # print()
        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request, f" your account profile updated")
            return redirect('profile')

    else:
        update_user_form = UserUpdateForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)
    content = {
        'u_form': update_user_form,
        'p_form': update_profile_form
    }
    return render(request, 'users/profile.html', content)
