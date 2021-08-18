from admin_app.models import MyUser
from django.contrib import admin
from .models import AdminAccount

# Register your models here.
admin.site.register(AdminAccount)
