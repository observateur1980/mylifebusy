from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# mylifebusy.com DB

class Contact(models.Model):
    full_name = models.CharField(max_length = 50)
    position = models.CharField(max_length = 50)
    office = models.CharField(max_length = 50)
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"









# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=40)
    thumbnail_url = models.CharField(max_length=400)
    icon = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Icon(models.Model):
    title = models.CharField(max_length=40)
    icon_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'icon'
        verbose_name_plural = 'icons'


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategory')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    thumbnail_url = models.CharField(max_length=400)
    book_count = models.IntegerField(default = 0)
    created_date = models.DateTimeField(default=timezone.now)
    booked_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'


class CareerMail(models.Model):
    full_name = models.CharField(max_length=200)
    email =     models.EmailField(max_length=200) 
    phone = models.CharField(max_length=20)
    looking_for = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/',
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    reference = models.CharField(max_length=300)
    def __str__(self):
        return self.email  