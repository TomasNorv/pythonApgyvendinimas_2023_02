from django.db import models

# Create your models here.
class Apgyvendinimas(models.Model):
    type = models.ForeignKey(to="Informacija", on_delete= models.SET_NULL, null= True, verbose_name='Nakvynės tipas',max_length=200)
    address = models.CharField(verbose_name='Adresas', max_length=200)
    city = models.CharField(verbose_name='Miestas', max_length=100)
    street = models.CharField(verbose_name='Gatvė', max_length=200)
    housenumber = models.CharField(verbose_name='Namo numeris', max_length=100)
    summary = models.TextField(verbose_name='Aprašymas', max_length= 5000)

class Informacija(models.Model):
    ad_type = models.CharField(verbose_name='Nakvynės tipas',max_length=200, help_text='Įveskite nakvynės tipą (pvz. apartamentai)')
    phone_nr = models.CharField(verbose_name="Tel. numeris", max_length=50)
    rooms = models.CharField(verbose_name="Kambariai", max_length=3)
    area = models.CharField(verbose_name='Plotas m2', max_length=10)
    amenities =models.TextField(verbose_name="Patogumai", max_length=3000)





# class NakvynesTipas(models.Model):
#     name= models.CharField(verbose_name= 'Nakvynės tipas', max_length=200, help_text='Įveskite nakvynės tipą (pvz. apartamentai)')
#
