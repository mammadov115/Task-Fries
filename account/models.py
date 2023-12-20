from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        COLLEAGUE = 'colleague', 'Colleague'
        CUSTOMER = 'customer', 'Customer'
        FREELANCER = 'freelancer', 'Freelancer'
    
    base_role = Role.ADMIN
    
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)

class Admin(User):
    base_role = User.Role.ADMIN

    class Meta:
        verbose_name = "Admin"

class Colleague(User):
    base_role = User.Role.COLLEAGUE

    class Meta:
        verbose_name = "Colleague"

class Customer(User):
    base_role = User.Role.CUSTOMER

    class Meta:
        verbose_name = "Customer"

class Freelancer(User):
    base_role = User.Role.FREELANCER
    age = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Freelancer"



# class ColleagueProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class CustomerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# class FreelancerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)