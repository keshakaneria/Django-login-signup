from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.conf import settings
from searchableselect.widgets import SearchableSelect
from .models import invite_form
from dal import autocomplete


class home_page(forms.Form):
    """Random home page to redirect the login and signup page to check its working"""
    pass


class signup_form(UserCreationForm):
    """To sign up a new account for new users"""
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class TimeInput(forms.TimeInput):
    """To display the time slot in time datatype"""
    input_type = 'time'


class invitation_form(forms.ModelForm):
    """Invitor invites users for meetings in particular time slot for decided agenda"""

    # invitees = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='user-autocomplete')
    # )

    # invitees = forms.ChoiceField(choices=userlist)

    class Meta:
        model = invite_form
        fields = ('invitees', 'time_slot', 'meeting_length', 'agenda')
        widgets = {
            'time_slot': TimeInput(),
            'invitees': autocomplete.ModelSelect2Multiple(url='user-autocomplete/'),
            # 'invitees': forms.Select(choices=mylist),
            # 'invitees': SearchableSelect(model=settings.AUTH_USER_MODEL, search_field='invitees',many=True),
        }
