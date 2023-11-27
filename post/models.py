from django.db import models

class Product(models.Model):
  image = models.ImageField(upload_to='products', null=True,blank=True)
  name = models.CharField(max_length=100)
  price = models.FloatField(default=0)
  net_weight = models.FloatField(null=True, blank=True)
  ingredients = models.TextField(null=True, blank=True)
  date_marking = models.DateField(null=True, blank=True)
  category = models.ForeignKey(
    'post.Category',
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    related_name='products'
  )
  def __str__(self) -> str:
    return f"{self.id} {self.name}"

class Category(models.Model):
  name = models.CharField(max_length=100)
  created_date = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f" Category: {self.name}"

class Review(models.Model):
  text = models.TextField()
  created_date = models.DateTimeField(auto_now=True)
  updated_date = models.DateTimeField(auto_now=True)
  product = models.ForeignKey(
    'post.Product',
    on_delete=models.CASCADE,
    blank=True,
    null=True,
    related_name="reviews"
  )
