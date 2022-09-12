from django.db import models

# Create your models here.
class Item(models.Model):
    """Representation of an item from online-store"""
    name = models.CharField(
        max_length=150,
        unique=True
    )
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"id={self.pk}, {self.name}"