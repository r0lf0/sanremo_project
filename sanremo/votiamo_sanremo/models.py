from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator


class Concorrente(models.Model):
    nome = models.CharField(max_length=50)
    canzone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Concorrenti"


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorie"


class Voto(models.Model):
    concorrente = models.ForeignKey(Concorrente, on_delete=models.CASCADE)
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    voto_outfit = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    voto_interpretazione = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    voto_canzone = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return ("Outfit:" + str(self.voto_outfit) + ",Interpretazione:" + str(self.voto_interpretazione) + ",Canzone:" + str(self.voto_canzone))

    class Meta:
        verbose_name_plural = "Voti"
        unique_together = ("concorrente", "utente")
