from django.db import models

class ProductCategory(models.Model):
	name = models.CharField(max_length=50, verbose_name = "Назва категорії")
	slug = models.SlugField(max_length=50)

	class Meta: 
		verbose_name = "Категорія"
		verbose_name_plural = "Категорії"

	def __str__(self):
		return 'Категорія %s' % self.name
'''
class EarningsBattery(models.Model):
	earnings = models.PositiveSmallIntegerField(default = 7, verbose_name = "Націнка %")

	def __str__(self):
		return 'Націнка %s' % self.earnings
'''
