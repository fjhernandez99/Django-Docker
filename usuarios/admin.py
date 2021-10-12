from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.models import Usuario
# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = ( 
        ('Datos del trabajador:', {'fields': ('first_name', 'last_name', 'username', 'email', 'age', 'password' , 'photo', 'role' )}),
        ('Permisos:', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Registro del usuario:', {'fields': ('last_login', 'date_joined')}),
     )
    list_display = ('username', 'first_name', 'last_name', 'email', 'age', 'role' )
    list_filter = ('username', )

admin.site.register(Usuario, UserAdmin)