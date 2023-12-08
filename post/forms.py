from django import forms
from post.models import Product, Category, Review



class ProductCreateForm(forms.Form):
  name = forms.CharField(max_length=100)
  price = forms.FloatField(max_value=10000, min_value=0)
  ingredients = forms.CharField(widget=forms.Textarea)
  image = forms.ImageField()

class ProductCreateForm2(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price','ingredients', 'image']

class  CategoryCreateForm(forms.Form):
  name = forms.CharField(max_length=100)


class ReviewCreateForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
