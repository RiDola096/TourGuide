from django.shortcuts import render, redirect

from guide.models import Guide
from .forms import GuideSignupForm, GuideEditForm
from django.contrib.auth import login


def guide_signup(request):
    if request.user.is_authenticated:
        return redirect('guides')
    signup_form = GuideSignupForm()
    print(signup_form.fields['password'])
    context = {
        'form': signup_form,
        'submit_button_text': 'Sign Up',
    }

    if request.method == 'POST':
        signup_form = GuideSignupForm(request.POST, request.FILES)
        if signup_form.is_valid():
            guide = signup_form.save()
            login(request, guide.user)
            return redirect('account')
    
    return render(request, 'signup.html', context)

def guide_edit(request):
    profile = Guide.objects.get(id=request.user.guide.id)
    edit_form = GuideEditForm()
    context = {
        'form': edit_form,
        'submit_button_text': 'Save',
    }

    if request.method == 'POST':
        edit_form = GuideEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            guide = edit_form.save(commit=False)
            profile.bio = guide.bio
            profile.location = guide.location
            profile.price = guide.price
            profile.save()
            return redirect('account')
    
    return render(request, 'guide/edit.html', context)
