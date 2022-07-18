from django.db import models

# Create your models here.
class Life_Expectancy(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    indicator_name = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100)
    age = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.country_name

    
    class Meta:
        verbose_name_plural = "Life Expectancy"