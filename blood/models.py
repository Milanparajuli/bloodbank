from django.db import models
# from user.models import User

# Create your models here.


class BloodGroup(models.Model):
    bloodgroupName = models.CharField(max_length=3)

    def __str__(self):
        return self.bloodgroupName

