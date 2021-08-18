from django.contrib.auth.models import AbstractUser
from django.db import models
from account.models import MyUser
# Create your models here.


class AdminAccount(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, primary_key=True)
    registration_code = models.CharField(max_length=50)
    is_admin_account = models.BooleanField(default=True)

    def __str__(self):
        return self.user.company_name
