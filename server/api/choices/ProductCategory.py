from django.db import models


class ProductCategory(models.TextChoices):
    PC = '01', 'PC・周辺機器'
    OFFICE_SUPPLIES = '02', 'オフィス用品'
    HOME_APPLIANCES = '03', '家電'
