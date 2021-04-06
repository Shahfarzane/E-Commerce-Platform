from django.db import models

# creating models for categories

class Category(models.Model):
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
# here we set the plural or singular name for categories
    class Meta:
        verbose_name_plural = 'Categories'


# here we show the name of the category instead of objects
    def __str__(self):
        return self.title


class Product(models.Model):
    # here we connect the category to the product.... on delete means if i delete the category i also delete the product.
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()        

def __str__(self):
    return self.title


