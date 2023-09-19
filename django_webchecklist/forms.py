from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# form classes
class CreateUserForm(UserCreationForm):
    captcha = ReCaptchaField()
    helper = FormHelper()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # defining a helper constructor
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    # customizing error messages
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is invalid")
        if len(email) >= 300:
            raise forms.ValidationError("Email too long")
