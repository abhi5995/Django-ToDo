from django.contrib import admin
from app1 import models

# Register your models here.
@admin.register(models.Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuname','stuemail', 'stuphone')