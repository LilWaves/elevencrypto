from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from captcha.fields import CaptchaField

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'login-input', 'name': 'username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login-input', 'name': 'password'}))

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'signup-input', 'name': 'username'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'signup-input', 'name': 'email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'signup-input', 'name': 'first_name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'signup-input', 'name': 'last_name'}))
    password1 = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'signup-input', 'name': 'password'}))
    password2 = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class': 'signup-input', 'name': 'repeat_password'}))
    #captcha = CaptchaField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
