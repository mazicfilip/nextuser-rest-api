from django.db import models


class Website(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True, null=False, blank=False)
    developmentMode = models.BooleanField()
    supportEmail = models.EmailField()
    noReplyEmail = models.EmailField()
    developerEmail = models.EmailField()
    timezone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
