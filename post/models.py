from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField(default=0)
  net_weight = models.FloatField(null=True, blank=True)
  ingredients = models.TextField(null=True, blank=True)
  date_marking = models.DateField(null=True, blank=True)

  def __str__(self) -> str:
    return f"{self.id} {self.name}"


