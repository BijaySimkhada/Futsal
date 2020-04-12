from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserInfo, FutsalInfo
# Register your models here.


class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'username', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'first_name', 'last_name', 'phone')
    search_fields = ('account_id', 'first_name', 'phone')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class FutsalInfoAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'futsal_name', 'location', 'price', 'phone')
    search_fields = ('account_id', 'futsal_name', 'location')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(FutsalInfo, FutsalInfoAdmin)