from django.db import models


# Create your models here.
class Order(models.Model):
    product_id = models.CharField(max_length=5)
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product_id = models.CharField(max_length=5)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name}'


class LastComments(models.Model):
    product_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Last comment by {self.name}'
