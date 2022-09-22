from django.db import models


class Item(models.Model):
    """Модель предмета."""
    name = models.CharField(max_length=50)
    description = models.TextField(help_text='Описание товара.')
    price = models.PositiveIntegerField(
        default=0,
        help_text='Цена товара в центах'
    )

    def __str__(self):
        return self.name
