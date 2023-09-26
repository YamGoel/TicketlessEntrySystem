from django.contrib import admin
from .models import Users,Unique
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['id','name','email','password']
admin.site.register(Users,UsersAdmin)


class UniqueAdmin(admin.ModelAdmin):
    search_fields=['uid']
    list_display=['uid']
admin.site.register(Unique,UniqueAdmin)

