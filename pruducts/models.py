from django.db import models
# Create your models here.

class Bolim(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField(null=True)
    def __str__(self):
        return self.title
#Bolimlar qismida mahsulotning qaysi bolimga tegishli ekanligini aniqlaymiz



class Products(models.Model):
    title = models.CharField(max_length=30)
    img = models.FileField(null=True)
    description = models.CharField(max_length=90, null=True, blank=True)
    come_data = models.DateField(auto_now_add=True)
    valid_date = models.DateField(blank=True)
    price = models.PositiveIntegerField()
    from_bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
#Pruduct bolimida Mahsulotning batafsil malumotlari kiritiladi sotuvchi qo'shilmadi so'ralmagani sababli