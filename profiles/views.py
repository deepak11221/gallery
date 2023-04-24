from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.


def add_profile(request):
    # add person form
    form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('profile.html')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'profiles/add_profile.html', ctx)
 
def view_profile(request, id):
    profile = Profile.objects.filter(user=request.user)
    if not profile:
        return redirect('add_profile')
    ctx = {'profile': profile}
    return render(request, 'profiles/view.html', ctx)



def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'profiles/edit.html', ctx)

def delete_profile(request, id):    
    profile = Profile.objects.get(id=id)
    profile.delete()
    messages.success(request, 'Your details added successfully')
    return redirect('profile')

