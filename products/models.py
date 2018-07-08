import random
import os
from django.db import models

def get_filename_extension(filename):
  basename = os.path.basename(filename)
  name, ext = os.path.splitext(basename)
  return name, ext

def upload_image_path(instance, filename):
  new_filename = random.randint(1, 9876421)
  name, ext = get_filename_extension(filename)
  final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
  return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

# Create your models here.
class FeaturedProductManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(is_featured=True)

class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=20, default=4.99)
  slug = models.SlugField(blank=True, unique=True) 
  product_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  is_featured = models.BooleanField(default=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  def get_absolute_url(self):
    return reverse('product_detail', kwargs={'slug': self.slug})
    # return "/products/{slug}/".format(slug=self.slug)

  objects = models.Manager()
  featured_products = FeaturedProductManager()

  def __str__(self):
    return self.title