from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    U_name = models.CharField(max_length=250)
    Reg_no = models.CharField(max_length=100)
    specs = models.CharField(max_length=110)
    email = models.CharField(max_length=200)
    mob_no = models.CharField(max_length=200)
    password = models.CharField(max_length=200)



    def __str__(self):
        return self.U_name + ' : ' + self.Reg_no


class Supervisor(models.Model):
    S_name = models.CharField(max_length=100)
    UId_no = models.CharField(max_length=100)
    specs = models.CharField(max_length=110)
    email = models.CharField(max_length=200)
    mob_no = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.S_name + ' : ' + self.UId_no

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Reg_no = models.CharField(max_length=10)
    specs = models.CharField(max_length=100)
    mob = models.CharField(max_length=10)
    sup_name = models.CharField(max_length=100,null=True)

class Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Uid = models.CharField(max_length=10)
    spec = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Data.objects.create(user=instance)
    instance.profile.save()
    instance.data.save()
