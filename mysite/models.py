from django.db import models

#onetoone relationship
# Create your models here.
class Female_Group(models.Model): 
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Male_Group(models.Model):
    name = models.CharField(max_length=100)
    women = models.OneToOneField(Female_Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
#onetomany relationship
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=100,null=True)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

#manytomany relationship
class Video(models.Model):
    title = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.title
    
class UserName(models.Model):
    name = models.CharField(max_length=100,null=True)
    watch = models.ManyToManyField(Video,null=True)
    def __str__(self):
        return self.name
    
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username