from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from users.models import User
# Register your models here.


@admin.register(User)
class CustomUserAdmin(EmailUserAdmin):
    model = User
    list_display = ('email', 'date_of_birth',)
