from django.db import models
#from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField("Название статьи", max_length=50)
    text = models.TextField("Текст")
    description = models.TextField("Описание статьи", null=True)
    date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"