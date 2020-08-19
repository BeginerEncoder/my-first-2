from django import forms
from Shop.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'product_text', 'product_image', 'product_price')