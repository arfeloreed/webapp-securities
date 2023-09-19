from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# url paths
urlpatterns = [
    path("", views.index, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("account-locked/", views.account_locked, name="account-locked"),
    # password management
    # url path for submitting a request form for password reset
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="webapp_securities/reset-password.html"
        ),
        name="password_reset",
    ),
    # url path for success message of email sent for password reset
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="webapp_securities/reset-password-sent.html"
        ),
        name="password_reset_done",
    ),
    # url path for sending an email link to reset the password
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="webapp_securities/reset-password-form.html"
        ),
        name="password_reset_confirm",
    ),
    # url path for message confirmation of successful password reset
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="webapp_securities/reset-password-done.html"
        ),
        name="password_reset_complete",
    ),
]
