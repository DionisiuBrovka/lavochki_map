from django import forms

class AddLavochkaForm(forms.Form):
    x = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    disc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    photo = forms.ImageField()