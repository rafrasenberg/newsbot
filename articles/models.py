from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    image = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)  

    def __str__(self):
        return self.title

        