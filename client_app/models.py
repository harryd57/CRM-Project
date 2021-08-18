from django.db import models
from account.models import MyUser


# Create your models here.


class ClientAccount(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, primary_key=True)
    phone_no = models.IntegerField()
    website = models.URLField(max_length=100)
    location = models.CharField(max_length=200)
    is_client_account = models.BooleanField(default=True)

    def __str__(self):
        return self.user.company_name
