"""
Definition of urls for DotDjango.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
dummy_aspects=[{'name':'management', 'aspects':['a','aa', 'aaa', 'aaaa']},
               {'name':'character', 'aspects':['b','bb', 'bbb', 'bbbb']}]
dummy_people=[{'name':'alice'}, {'name':'bob'}, {'name':'carol'}]
urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^signup', django.contrib.auth.views.login,
       {
           'template_name':'app/signup.html',
           'authentication_form': app.forms.BootstrapSignupForm, 
           'extra_context':{'year':datetime.now().year}
        },
        name='signup'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^creategroup$',
        django.contrib.auth.views.login,
       {
           'template_name':'app/creategroup.html',
           'authentication_form': app.forms.BootstrapGroupForm,
           'extra_context':{'year':datetime.now().year}
        },
        name='creategroup'),
    url(r'^adddot$',
        django.contrib.auth.views.login,
       {
           'template_name':'app/adddot.html',
           'authentication_form': app.forms.BootstrapAdddotForm,
           'extra_context':{'people':dummy_people, 'aspects':dummy_aspects, 'year':datetime.now().year}
        },
        name='adddot'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
