from django.db import models

# Create your models here.    
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Image(models.Model):
    file=models.ImageField(upload_to='images/')
    Category=models.ForeignKey(Category, on_delete= models.CASCADE ,related_name="images")
    tags=models.ManyToManyField(Tag,related_name='images')
    def __str__(self):
        return self.file.name
    

