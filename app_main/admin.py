from django.contrib import admin
from .models import Tag, RPGSystem

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...

@admin.register(RPGSystem)
class RPGSystemAdmin(admin.ModelAdmin):
    ...