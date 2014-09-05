from django.db import models
import datetime
from django.core import exceptions

def validate_date_later(value):
    if value<datetime.date.today():
        raise exceptions.ValidationError(_('You cannot choose a Scheduled time later than now'))


# Create your models here.

class Accounts_Developer(models.Model):
    email_address=models.EmailField(max_length=254,primary_key=True)
    name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=20)
    balance=models.IntegerField(max_length=11)
    last_login_date=models.DateTimeField()
    hash=models.CharField(max_length=250)
    salt=models.CharField(max_length=250)
    account_id=models.CharField(max_length=30)
    active=models.BooleanField(default=False)
    payment_plan=models.CharField(max_length=30)
    api_key=models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.email_address