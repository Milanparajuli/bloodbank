from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from blood.models import BloodGroup


class UserManager(BaseUserManager):
    def create_user(self, email,name ,contact_no,bloodGroup,citizenShipNo, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            contact_no=contact_no,
            bloodGroup=bloodGroup,
            citizenShipNo=citizenShipNo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,contact_no,bloodGroup,citizenShipNo, password=None):

        user = self.create_user(
            email,
            name,
            contact_no,
            bloodGroup,
            citizenShipNo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact_no = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True,null=True)
    bloodGroup = models.ForeignKey(BloodGroup,on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    citizenShipNo = models.CharField(max_length=100,unique=True)
    about = models.TextField(blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','contact_no','bloodGroup','citizenShipNo']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin