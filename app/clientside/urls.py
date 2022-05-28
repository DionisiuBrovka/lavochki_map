from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', pg_index),
    path('add_form', pg_add_form),
    path('edit_form', pg_index),
    path('auth', pg_auth),
    path('api/points', pg_api_points),
    path('login', MyLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('signup', Signup.as_view(), name = 'signup'),
    path('confirm_email', TemplateView.as_view(template_name='registration/confirm_email.html'),
        name='confirm_email'),
    path('verify_email/<uidb64>/<token>',
        EmailVerify.as_view(),
        name='verify_email',
        ),
    path('invalid_verify',
        TemplateView.as_view(template_name='registration/invalid_verify.html'),
        name='invalid_verify'
        
    ),
]