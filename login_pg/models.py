from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from multiselectfield import MultiSelectField


class register_details(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    mailid = models.EmailField(max_length=50)
    pswrd = models.CharField(max_length=50)


class invite_form(models.Model):
    """Fields for invitation form is created with its particular datatype"""
    # invitees = models.SlugField(error_messages={'required': 'No record found!'})
    # invitees = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,error_messages={'required': 'No record found!'})
    userlist = ()
    c=0
    for i in User.objects.all():
        userlist+=((str(i),str(i)),)
        c+=1
    print(userlist)
    # invitees = models.ManyToManyField(User)
    invitees = models.CharField(max_length=50)
    # invitees = MultiSelectField(choices= userlist)
    time_slot = models.TimeField()
    meeting_length = models.PositiveIntegerField(default=0)
    agenda = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.agenda        
