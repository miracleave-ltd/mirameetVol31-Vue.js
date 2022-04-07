from django.db import models


class ProductSubCategory(models.TextChoices):
    NOTE_PC = '01', 'ノートパソコン'
    DESKTOP_PC = '02', 'デスクトップパソコン'
    DISPLAY = '03', 'ディスプレイ'
    NOTEBOOK = '04', 'ノート'
    POCKET_BOOK = '05', '手帳'
    WRITING_UTENSILS = '06', '筆記用具'
    MICROWAVE_OVEN = '07', '電子レンジ'
    REFRIGERATOR = '08', '冷蔵庫'
    AIR_CONDITIONER = '09', 'エアコン'
