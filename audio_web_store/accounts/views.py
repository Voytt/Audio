from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def account_registration_view(request):
    if request.method == "POST":
        userCreationForm = UserCreationForm(request.POST)
        if userCreationForm.is_valid():
            userCreationForm.save()
            return redirect("products_home_view")
    else :
        userCreationForm = UserCreationForm()
    context = {
        "userCreationForm": userCreationForm
    }
    return render (request, "accounts/account_registration.html", context)
