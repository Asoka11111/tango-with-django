from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)

class  PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category',{'fields': 'category'}),
        ('Page Name', {'fields': 'title'}),
        ('URL', {'fields': 'url'}),        
    ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}
