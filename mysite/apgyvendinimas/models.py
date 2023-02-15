from django.db import models

# Create your models here.
class Objektas(models.Model):
    caption = models.CharField(verbose_name= "Antraštė", max_length=100)
    type = models.CharField(verbose_name='Nakvynės tipas', max_length=200, help_text='Įveskite nakvynės tipą (pvz. apartamentai, studija, butas)')
    phone_nr = models.CharField(verbose_name="Tel. numeris", max_length=30,help_text='Įveskite Tel. nr. (pvz. +370x xxxxxxx )')
    address = models.CharField(verbose_name='Adresas', max_length=200)
    city = models.CharField(verbose_name='Miestas', max_length=100)
    street = models.CharField(verbose_name='Gatvė', max_length=200)
    housenumber = models.CharField(verbose_name='Namo numeris', max_length=100)
    rooms = models.CharField(verbose_name="Kambariai", max_length=3)
    area = models.CharField(verbose_name='Plotas m2', max_length=10)
    max_guest = models.CharField(verbose_name= 'Maks. svečiai', max_length= 10)
    summary = models.TextField(verbose_name='Aprašymas', max_length= 5000)
    amenities = models.TextField(verbose_name="Patogumai", max_length=5000)



    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Objektas'
        verbose_name_plural = 'Objektai'



