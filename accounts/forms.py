from django import forms
# from .models import UserModel
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.core.validators import MinLengthValidator


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required = True)
    password = forms.CharField(validators=[MinLengthValidator(8, 'the filed must contain at least 8 characters')])
    
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.password = self.cleaned_data["password"]
        if commit:
            user.save()
        return user
            