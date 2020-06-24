from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Wpis(models.Model):
    name = models.CharField(max_length=150)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="nalezace")
    note = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.name