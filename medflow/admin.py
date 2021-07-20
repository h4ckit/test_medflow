from medflow.models import User, Doctor, DeltaTime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# class UsersAdmin(UserAdmin):
#     model = User
#     list_display = ('email', 'is_staff', 'is_active',)
#     ordering = ['email']
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#     )
#
#
# admin.site.register(User, UsersAdmin)
# admin.site.register(Doctor, admin.ModelAdmin)
# admin.site.register(DeltaTime, admin.ModelAdmin)
