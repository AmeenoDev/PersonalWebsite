from django.db import models
from datetime import datetime
# Create your models here.
class Product(models.Model):
    catagory_choices = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
    ]
    name= models.CharField(max_length=100,default='Product Name',null=False,verbose_name='title')
    description = models.TextField(default='Product Description',null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image = models.ImageField(upload_to='blogs/images/%y/%m/%d/',default='staticfiles/assets/images/banner-01.jpg')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=catagory_choices)
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        
class Test(models.Model):
    date =models.DateField()
    time = models.TimeField(null=True)
    create = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.date)