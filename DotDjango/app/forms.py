"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapGroupForm(AuthenticationForm):

    group_name = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Group Name'}))

class BootstrapSignupForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    email = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Last Name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapAdddotForm(AuthenticationForm):

    comments = forms.CharField(widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Comments'}))
    scale = forms.CharField(widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Scale'}))
    importance = forms.CharField(widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Importance'}))


