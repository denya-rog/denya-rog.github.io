from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(primary_key = True, max_length=64)

    def __str__(self):
        try:
            return 'user:%s... with mail: %s' % (self.name, self.email)
        except:
            return self.user.username

    class Meta:
        verbose_name = "MySubscriber"
        verbose_name_plural = "All " + verbose_name + "s"
