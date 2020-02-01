from django.db import models

class Account_Page(models.Model):
    name = models.CharField(max_length=40)
    slug  = models.CharField(max_length=20)
    page_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Ad_Account(models.Model):
    name = models.CharField(max_length=40)
    slug  = models.CharField(max_length=20)
    page_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name