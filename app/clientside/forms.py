from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class AddLavochkaForm(forms.Form):
    x = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    disc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    photo = forms.ImageField()

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label = ("Email"),
        max_length = 254,
        widget = forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")