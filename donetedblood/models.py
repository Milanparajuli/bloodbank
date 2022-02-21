from django.db import models
from user.models import User
from user.models import BloodGroup

# Create your models here.
class BloodBank(models.Model):
    donatedDate = models.DateField(auto_now=True)
    expiryDate = models.DateField()
    bloodgroup = models.ForeignKey(BloodGroup,on_delete= models.CASCADE)
    dondatetBy = models.ForeignKey(User,on_delete=models.CASCADE)

    def __init__(self):
        return self.donatetBy.name
