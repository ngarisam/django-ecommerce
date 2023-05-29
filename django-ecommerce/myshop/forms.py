from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
class CustomerLoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Passsword',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    
class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Passsword',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class  MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))

    pass
class PasswordResetConfirm(PasswordResetForm()):
    pass
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','mobile','county']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'county':forms.Select(attrs={'class':'form-control'}),
                }
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'autofocus':True,'autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autofocus':True, 'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'autofocus':True, 'autocomplete':'current-password','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autofocus':True, 'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'autofocus':True, 'autocomplete':'current-password','class':'form-control'}))


