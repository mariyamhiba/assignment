from django.contrib import admin

# Register your models here.
from .models import user_login,user,student_details

admin.site.register(user_login)
admin.site.register(user)
admin.site.register(student_details)
