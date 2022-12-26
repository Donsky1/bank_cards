from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_display_links = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    ordering = ('-id', )


admin.site.register(MyUser, MyUserAdmin)