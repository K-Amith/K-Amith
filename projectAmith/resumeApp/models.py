from django.db import models

# Create your models here.







class MyObjective(models.Model):
    obj_id=models.AutoField(primary_key=True)
    objctive=models.CharField(max_length=2048,unique=True)
    def __int__ (self):
        return self.obj_id

class MyProfile(models.Model):
    mp_id=models.AutoField(primary_key=True)
    profile=models.CharField(max_length=2048,unique=True)
    def __int__ (self):
        return self.mp_id


class Skill(models.Model):
    s_id=models.AutoField(primary_key=True)
    skills=models.CharField(max_length=1024,unique=True)
    def __str__ (self):
        return self.skills

class Award(models.Model):
    a_id=models.AutoField(primary_key=True)
    awards=models.CharField(max_length=1024,unique=True)
    def __str__ (self):
        return self.awards

class Workshop(models.Model):
    w_id=models.AutoField(primary_key=True)
    workshop=models.CharField(max_length=1024,unique=True)
    def __str__ (self):
        return self.workshop

class Hobbie(models.Model):
    h_id=models.AutoField(primary_key=True)
    hobbies=models.CharField(max_length=1024,unique=True)
    def __str__ (self):
        return self.hobbies


class PersonalDetail(models.Model):
    pd_id=models.AutoField(primary_key=True)
    topic=models.CharField(max_length=1024,unique=True)
    detail=models.CharField(max_length=1024)
    def __str__ (self):
        return self.topic

class Project(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_heading=models.CharField(max_length=1024,unique=True)
    p_title=models.CharField(max_length=1024)
    p_discription=models.CharField(max_length=2048)
    p_subhead1=models.CharField(max_length=1024)
    p_sub_1_discription=models.CharField(max_length=2048)
    p_subhead2=models.CharField(max_length=1028)
    p_sub_2_discription=models.CharField(max_length=2048)
    skill_set=models.ForeignKey(Skill,on_delete=models.CASCADE)
    def __str__ (self):
        return self.p_title

class Feed_back(models.Model):
    f_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=256);
    email_id=models.CharField(max_length=256,unique=True);
    feed_back=models.CharField(max_length=2048);
    def __int__ (self):
        return self.f_id
