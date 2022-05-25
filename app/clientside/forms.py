from django import forms

class AddLavochkaForm(forms.Form):
    x = forms.FloatField()
    y = forms.FloatField()
    disc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    photo = forms.ImageField()