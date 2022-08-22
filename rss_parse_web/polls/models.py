from django.db import models


class News(models.Model):
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200)
    details = models.CharField(max_length=4000)
    published = models.DateField()


class Media(models.Model):
    link = models.CharField(max_length=1000)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
