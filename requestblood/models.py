from django.db import models
from blood.models import BloodGroup
from user.models import User

# Create your models here.
priority_choices = [('high','High'),('medium','Medium'),('low','Low')]
class BloodRequest(models.Model):
    bloodgroup = models.ForeignKey(BloodGroup,on_delete=models.CASCADE)
    requetedDate= models.DateField(auto_now=True)
    location = models.CharField(max_length=100,)
    quantity = models.FloatField(default=1.5)
    requestedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    priority = models.CharField(max_length=20,choices=priority_choices)
    description = models.TextField(null=True,blank=True)
    isReceived = models.BooleanField(default=False)

    def __init__(self):
        return self.requestedBy.name
