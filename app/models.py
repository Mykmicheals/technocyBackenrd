from django.core.validators import validate_comma_separated_integer_list, MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from operator import mod
from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='media')
    header = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.header


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brands"


class AllModels(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    # specification = models.JSONField(null=True)
    image = models.ImageField(upload_to='media')
    slug = models.SlugField(unique=True)
    price = models.CharField(
        validators=[
            validate_comma_separated_integer_list],
        max_length=12,
    )
    star = models.IntegerField(
        validators=[MinValueValidator(3), MaxValueValidator(5)], default=4)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name[:50])
        super(AllModels, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Phone(AllModels):
    class Meta:
        verbose_name_plural = "Phones"


class PopularProducts(AllModels):
    class Meta:
        verbose_name_plural = "Popular Products"


class Laptops(AllModels):
    class Meta:
        verbose_name_plural = "Laptops"


class Television(AllModels):
    class Meta:
        verbose_name_plural = 'Televisions'
