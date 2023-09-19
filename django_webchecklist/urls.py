"""
URL configuration for django_webchecklist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # local apps
    path("", include("webapp_securities.urls")),
    # 2FA
    path("", include(tf_urls)),
    path("accounts/register/", views.register, name="register"),
    # logging out the user
    path("user-logout", views.user_logout, name="user-logout"),
]

# 2FA paths
# account/login/ [name='login']
# account/two_factor/setup/ [name='setup']
# account/two_factor/qrcode/ [name='qr']
# account/two_factor/setup/complete/ [name='setup_complete']
# account/two_factor/backup/tokens/ [name='backup_tokens']
# account/two_factor/ [name='profile']
# account/two_factor/disable/ [name='disable']

# all auth paths
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
