from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields
from django.forms import ModelForm
from .models import Session, User


class UserRegisterForms(UserCreationForm):  

    class Meta:
        model = User
        fields = ('username',
         'name',  
         'email', 
         'password1', 
         'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class ImageForm(ModelForm):

    class Meta:
        model = Session
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sl_no'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'YY-MM-DD'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control', 'placeholder': 'in hours'})

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'name', 'email', 'idcardno', 'phoneno']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['idcardno'].widget.attrs.update({'class': 'form-control'})
        self.fields['phoneno'].widget.attrs.update({'class': 'form-control'})

# class InfoProfile(forms.ModelForm):
#     class Meta():
#         model = Profile
#         fields = ('phone_Number', 'id_card_no', 'Gender')
