from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pictures_images")

    def __str__(self):
        return self.title
