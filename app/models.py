from django.db import models

class Detail(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()
    otp=models.IntegerField()
    mail=models.CharField(max_length=30)
    passw=models.CharField(max_length=20)
    rpass=models.CharField(max_length=20)


class Movie(models.Model):
    unique=models.IntegerField()
    movieimagelink=models.CharField(max_length=500)
    moviename=models.CharField(max_length=40)
    moviedate=models.DateField()
    description=models.TextField(max_length=1000)
    rating=models.IntegerField()
    director=models.CharField(max_length=200)
    actors=models.CharField(max_length=300)

    english=models.CharField(max_length=10)
    hindi=models.CharField(max_length=10)
    south=models.CharField(max_length=10)
    marathi=models.CharField(max_length=10)
    action=models.CharField(max_length=10)
    comedy=models.CharField(max_length=10)
    drama=models.CharField(max_length=10)
    advanture=models.CharField(max_length=10)
    romantic=models.CharField(max_length=10)
    link1=models.CharField(max_length=1000)
    link2=models.CharField(max_length=1000)
    link4=models.CharField(max_length=1000)


class Crausallink(models.Model):
    idunique=models.IntegerField()
    crausal1=models.CharField( max_length=200)
    crausal2=models.CharField( max_length=200)
    crausal3=models.CharField( max_length=200)
    crausal4=models.CharField( max_length=200)
    crausal5=models.CharField( max_length=200)

class Code(models.Model):
    code1=models.IntegerField()
    code2=models.IntegerField()
    code3=models.IntegerField()
    code4=models.IntegerField()


class TCode(models.Model):
    code1=models.IntegerField()
    code2=models.IntegerField()
    code3=models.IntegerField()
    code4=models.IntegerField()
    uid=models.IntegerField()


