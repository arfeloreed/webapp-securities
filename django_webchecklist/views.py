from django.contrib import auth, messages
from django.shortcuts import redirect, render

from .forms import CreateUserForm


# view route for user sign up page
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("two_factor:login")

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


# view route for user logout
def user_logout(request):
    auth.logout(request)

    messages.success(request, "Logout successful")

    return redirect("home")
