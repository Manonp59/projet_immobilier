from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from prediction.models import Estimation,User
from django.utils import timezone



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email','password1','password2')


class EstimationForm(forms.ModelForm):
    grade = forms.IntegerField(max_value=13, min_value=1)
    view = forms.IntegerField(min_value=0,max_value=4)
    condition = forms.IntegerField(min_value=1, max_value=5)
    
    class Meta:
        model = Estimation
        fields = [
            'titre',
            'm2_living',
            'm2_lot',
            'm2_above',
            'm2_basement',
            'bedrooms',
            'bathrooms',
            'floors',
            'zipcode',
            'grade',
            'view',
            'waterfront',
            'condition',
            'yr_renovated',
            'yr_built',
        ]
        widgets = {
            'zipcode': forms.Select(choices=Estimation.zip_choices),
            'waterfront' : forms.Select(choices = Estimation.waterfront_choices)
        }