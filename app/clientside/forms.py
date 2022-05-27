from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AddLavochkaForm(forms.Form):
    x = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    disc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    photo = forms.ImageField()

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User