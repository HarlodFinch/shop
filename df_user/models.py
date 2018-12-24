from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uresvaddress = models.CharField(max_length=30, default='')
    uaddress = models.CharField(max_length=100, default='')
    uems = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')