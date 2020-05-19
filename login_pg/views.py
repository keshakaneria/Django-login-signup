from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .forms import home_page, invitation_form, signup_form
from .models import invite_form
from dal import autocomplete


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = User.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
        

def home(request):
    """Calls the home page"""
    form = home_page()
    return render(request, 'home.html', {'home': form})


def login_request(request):
    """Authenticates the form from the databse by verifying entered data is correct or not"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.get(username__exact=username)
            # if hashed password is matched with database then checks for existance of username/passwrd
            if u.check_password(password):
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'home.html', {'username': username})
                else:
                    messages.error(request, "User does not exist!")
            # hashed password is not correct with database values
            else:
                messages.error(request, "Invalid password.")
        # form is not defined as per required instructions
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login-pg.html', {'log': form})


def logout_request(request):
    """Calls the logout function to end the session and bring back to login page"""
    logout(request)
    AuthenticationForm()
    return redirect('login')


def signup(request):
    """New user signing up function"""
    if request.method == 'POST':
        form = signup_form(request.POST)
        noform = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = make_password(form.cleaned_data.get('password1'))
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            MyUsers(user=username).save()
            return render(request, 'home.html', {'username': username})
    else:
        form = signup_form()
    return render(request, 'signup-pg.html', {'sign': form})


def invite(request):
    form = invitation_form()
    if request.method == 'POST':
        form = invitation_form(request.POST)
        inv_list = request.POST['invitees']
        t_slot = request.POST['time_slot']
        meeting_len = request.POST['meeting_length']
        aim = request.POST['agenda']
        inv_table = invite_form(invitees = inv_list, time_slot = t_slot, meeting_length = meeting_len, agenda = aim)
        username = request.user.username
        inv_table.save()
        return render(request, 'home.html', {'username': username})
    return render(request, 'invite-pg.html', {'inv': form})
