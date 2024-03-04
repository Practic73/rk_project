from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование валюты',
    )
    rate = models.DecimalField(
        max_digits=999,
        decimal_places=2,
        verbose_name='Курс валюты в рублях',
    )

    def __str__(self):
        return self.name
