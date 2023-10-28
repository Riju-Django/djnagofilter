import django_filters
from django import forms  # Import forms from Django
from django.contrib.auth.models import User

class table_filter_form(django_filters.FilterSet):
    username = django_filters.CharFilter(
        lookup_expr='iexact',
        widget=forms.TextInput(attrs={
            'class': 'form-control m-2',
            'type': 'text',
            'placeholder': 'Username'
        })
    )

    email = django_filters.CharFilter(
        lookup_expr='iexact',
        widget=forms.EmailInput(attrs={
            'class': 'form-control m-2',
            'type': 'email',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
