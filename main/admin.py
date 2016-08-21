from django.contrib import admin
from main.models import *


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('id', 'name')

	
admin.site.register(ProductCategory, CategoryAdmin)