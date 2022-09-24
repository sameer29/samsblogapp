from django.db import models

# Create your models here.

class BlogModel(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + ' ' + self.title

    class Meta:
        ordering = ['-pub_date']