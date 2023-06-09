from django.forms import ModelForm
from .models import Entries as Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email','is_staff','password1','password2']
        # fields = '__all__'
        print('dield',fields)