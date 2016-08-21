from django.db import models


'''
class TypeOfBattery(models.Model):
	TYPE_OF_BATTERY = (('SLI', 'CLASIC'), ('AGM', 'AGM'), ('GEL', 'GEL'))
	name = models.CharField(max_length = 10, verbose_name = "Тип акумулятора", choices = TYPE_OF_BATTERY, default = 'SLI')

	def __str__(self):
		return self.name
'''
		
class TypeOfBattery(models.Model):
	name = models.CharField(max_length = 10, verbose_name = "Тип акумулятора")
	slug = models.SlugField(max_length=10)
	type_info = models.TextField(max_length = 1000, blank = True)

	def __str__(self):
		return self.name		

'''
class BrandName(models.Model):
	BRAND_NAME = (('BOSCH', 'BOSCH'), ('VARTA', 'VARTA'), ('FIAMM', 'FIAMM'), ('JENOX', 'JENOX'))
	name = models.CharField(max_length = 50, verbose_name = "Виробник", choices = BRAND_NAME)

	def __str__(self):
		return self.name
'''

class BrandName(models.Model):
	name = models.CharField(max_length = 50, verbose_name = "Виробник")
	slug = models.SlugField(max_length=50)
	brand_info = models.TextField(max_length = 1000, blank = True)


	def __str__(self):
		return self.name

class Series(models.Model):
	brand = models.ForeignKey(BrandName)
	name = models.CharField(max_length = 50, verbose_name = "Серія")
	slug = models.SlugField(max_length=50)
	image = models.ImageField(upload_to = 'batteries/series', blank = True)
	series_info = models.TextField(max_length = 1000, blank = True)

	def __str__(self):
		return self.name		
			

class СarBatteries(models.Model):
	VOLTAGE_BATTERY = ((12,'12V'),(6,'6V'))
	category = models.ForeignKey('main.ProductCategory')
	battery_type = models.ForeignKey(TypeOfBattery)
	brand = models.ForeignKey(BrandName)
	series = models.ForeignKey(Series)
	voltage = models.PositiveSmallIntegerField(default = 12, verbose_name = "Напруга", choices = VOLTAGE_BATTERY)
	battery_model = models.CharField(max_length = 50, verbose_name = "Модель", blank = True)
	cold_cranking_amps = models.PositiveSmallIntegerField(verbose_name = "Пусковий струм, А")
	cranking_amps = models.PositiveSmallIntegerField(verbose_name = "Ємність, Ah")
	length = models.PositiveSmallIntegerField(verbose_name = "Довжина, мм", blank = True)
	width = models.PositiveSmallIntegerField(verbose_name = "Ширина, мм", blank = True)
	height = models.PositiveSmallIntegerField(verbose_name = "Висота, мм", blank = True)
	positive_terminal_side_right = models.BooleanField(default = True, verbose_name = "Полярність права", help_text = "Якщо акумулятор з привим плюсом залиште як є, якщо ні то заберіть галочку")
	weight = models.DecimalField(max_digits = 5, decimal_places = 1,  blank = True, verbose_name = "Вага, кг" )
	price = models.PositiveSmallIntegerField(verbose_name = "Ціна, грн")
	image = models.ImageField(upload_to = 'main/battery', default='main/battery/no_image_battery.jpg', blank = True)
	producer = models.CharField(max_length = 50, verbose_name = "Країна виробник", blank = True)
	warranty = models.PositiveSmallIntegerField(verbose_name = "Гарантія, міс.", blank = True)
	info = models.CharField(max_length = 50, verbose_name = "Примітка", blank = True)
	slug = models.SlugField(max_length=50)

	class Meta: 
		verbose_name = "Акумулятор"
		verbose_name_plural = "Акумулятори"

	def __str__(self):
		return 'Акумулятор %s' % self.category

	def earnings_price(self):
		new_price = self.price * 0.2 + self.price
		return round(new_price)