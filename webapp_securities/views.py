from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# view route for home page
def index(request):
    return render(
        request,
        "webapp_securities/index.html",
    )


# view route for dashboard page
@login_required()
def dashboard(request):
    return render(
        request,
        "webapp_securities/dashboard.html",
    )


# view route for account locked page
def account_locked(request):
    return render(
        request,
        "webapp_securities/account-locked.html",
    )
