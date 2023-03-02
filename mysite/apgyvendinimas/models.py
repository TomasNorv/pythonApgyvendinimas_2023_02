from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import date
from PIL import Image
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Objektas(models.Model):
    caption = models.CharField(verbose_name= _("Caption"), max_length=100)
    type = models.CharField(verbose_name=_('Type'), max_length=200, help_text=_('Enter the type of accommodation (e.g. apartment, studio, apartment)'))
    city = models.CharField(verbose_name=_('City'), max_length=100)
    address = models.CharField(verbose_name=_('Address'), max_length=200)

    street = models.CharField(verbose_name=_('Street'), max_length=200)
    housenumber = models.CharField(verbose_name=_('House number'), max_length=100)
    area = models.CharField(verbose_name=_('Area m2'), max_length=10)
    phone_nr = models.CharField(verbose_name=_("Phone nr"), max_length=30, help_text=_('Enter Phone. nr. (e.g. +370x xxxxxxx )'))
    rooms = models.CharField(verbose_name=_("Rooms"), max_length=3)
    max_guest = models.CharField(verbose_name= _('Max quest'), max_length= 10)
    price = models.FloatField(verbose_name=_("Daily price eur"))
    #description = models.TextField(verbose_name='Aprašymas', max_length= 5000, null=True, blank=True, default="")
    description = HTMLField(verbose_name=_('Description'), null=True, blank=True)
    amenities = models.TextField(verbose_name=_("Amenities"), max_length=5000, null=True, blank=True)
    foto = models.ImageField(verbose_name=_('Foto'),upload_to='foto', null=True, blank=True)
    user = models.ForeignKey(to=User, verbose_name=_("User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Object')
        verbose_name_plural = _('Objects')


class ObjektasReview(models.Model):
    objektas = models.ForeignKey(to='Objektas', verbose_name=_('Object'), on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    reviewer = models.ForeignKey(to=User, verbose_name=_('User'), on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name=_('Time'), auto_now_add=True)
    content = models.TextField(verbose_name=_('Reviews'), max_length=3000)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _('Reviews')
        ordering = ['-date_created']


class Profilis(models.Model):
    user = models.OneToOneField(verbose_name=_("User"), to=User, on_delete=models.CASCADE)
    foto = models.ImageField(verbose_name= _('Foto'), default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.foto.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.foto.path)


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _('Profiles')