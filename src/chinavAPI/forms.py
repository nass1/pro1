from django import forms
from django.forms import ModelForm
from .models import ProductsModels

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)



class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductsModels
        fields = ['product_name_mod', 'product_price_mod', 'overview_lst_mod']