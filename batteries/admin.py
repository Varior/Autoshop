from django.contrib import admin
from batteries.models import *



class BatteryAdmin(admin.ModelAdmin):    
	list_display = ('battery_type','brand', 'series','voltage','battery_model', 'price', 'earnings_price', 'info')
	fieldsets = (
		(None, {
			'fields': ('category', 'battery_type', 'brand', 'series', 'battery_model', 'image', 'voltage','slug')
		}),
		('Характеристики', {
			'fields': (('cranking_amps', 'cold_cranking_amps', 'positive_terminal_side_right', 'weight'), ),
		}),
		('Розмір', {
			'fields': (('length', 'width', 'height'), ),
		}),
		('Ціна\наявність', {
			'fields': (('price', 'warranty', 'info'))
		}),
	)
	prepopulated_fields = {'slug': ('brand', 'series', 'battery_model', 'cranking_amps', 'cold_cranking_amps')}
	search_fields = ('battery_model', 'info')
  

class TypeOfBatteryAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug': ('name',)}


class BrandNameAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug': ('name',)}

class SeriesAdmin(admin.ModelAdmin):
	list_display = ('brand', 'image', 'name')
	prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(СarBatteries, BatteryAdmin)
admin.site.register(TypeOfBattery, TypeOfBatteryAdmin)
admin.site.register(BrandName, BrandNameAdmin)
admin.site.register(Series, SeriesAdmin)