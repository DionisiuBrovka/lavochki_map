from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class AddLavochkaForm(forms.Form):
    x = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    disc = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    photo = forms.ImageField()

User = get_user_model()

class MyAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)

            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Почта не верифицирована. Проверьте вашу почту.',
                    code='invalid_login',
                )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        
        return self.cleaned_data

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label = ("Email"),
        max_length = 254,
        widget = forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")