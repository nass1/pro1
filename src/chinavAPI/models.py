from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField
from django.db import models
import ast


class ProductsModels(models.Model):
    product_id_mod = models.CharField(max_length=20,blank=True)
    product_name_mod = models.CharField(max_length=2000,blank=True)
    product_url_mod = models.CharField(max_length=20000,blank=True)
    product_price_mod = models.CharField(max_length=20000,blank=True)
    category_name_mod = models.CharField(max_length=20000,blank=True)
    overview_lst_mod = models.CharField(max_length=20000,blank=True)
    main_picture_mod = models.CharField(max_length=20000,blank=True)
    additional_images_mod = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.product_id_mod + "--- " + self.product_name_mod



