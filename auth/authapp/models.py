from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)


# user = User.objects.create_user(username="hanifi", password="hanifi")
# Employee.objects.create(user=user, company="Zack Ai")