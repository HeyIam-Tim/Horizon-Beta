from django.db import models


class MainStorage(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    main_storage = models.ForeignKey(MainStorage, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=355, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    unique_number = models.IntegerField(null=True, blank=True)
    qauntity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



