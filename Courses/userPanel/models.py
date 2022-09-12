from django.db import models

# Create your models here.

class slider(models.Model):
    sl_title = models.CharField(max_length=200)
    sl_pragraph = models.TextField(max_length=500)
    sl_image = models.FileField()

class found(models.Model):
    fnd_title = models.CharField(max_length=200)
    fnd_pragraph = models.CharField(max_length=200)
    fnd_image = models.ImageField()

class feature(models.Model):
    feat_name = models.CharField(max_length=50)
    feat_title = models.CharField(max_length=200)
    feat_pragraph = models.TextField(max_length=500)
    feat_image = models.ImageField()

class tips(models.Model):
    tps_title = models.CharField(max_length=200)
    tps_pragraph = models.TextField(max_length=500)
    tps_line = models.CharField(max_length=200)
    tps_file = models.FileField()

class subjects(models.Model):
    sub_name = models.CharField(max_length=50)
    sub_fee = models.CharField(max_length=50)
    sub_duration = models.CharField(max_length=50)
    sub_details = models.TextField(max_length=500)
    sub_image = models.ImageField()

class community(models.Model):
    com_name = models.CharField(max_length=50)
    com_pragraph = models.TextField(max_length=500)
    com_address = models.CharField(max_length=150)
    com_details = models.TextField(max_length=500)
    com_image = models.ImageField()

class guideline(models.Model):
    guid_title = models.CharField(max_length=200)
    guid_pragraph = models.TextField(max_length=500)
    guid_file = models.FileField()
    date_time = models.DateTimeField(auto_now_add=True)

class blogs(models.Model):
    blog_name =  models.CharField(max_length=50)
    blog_title =  models.CharField(max_length=200)
    blog_details =  models.TextField(max_length=1500)
    blog_comment = models.CharField(max_length=500)
    blog_image = models.ImageField()

class comments(models.Model):
    comm_person_name =  models.CharField(max_length=50)
    comm_person_email =  models.EmailField(max_length=150)
    comm_person_website =  models.URLField()
    comm_detils =  models.TextField(max_length=500)
    comm_date =  models.DateField()
    comm_time =  models.TimeField()
    comm_person_image = models.ImageField()
    commnts_id = models.ForeignKey(blogs,on_delete=models.CASCADE)

class reply(models.Model):
    rply_person_name = models.CharField(max_length=50)
    rply_details = models.TextField(max_length=500)
    rply_date = models.DateField()
    rply_time = models.TimeField()
    rply_person_image = models.ImageField()
    rply_id = models.ForeignKey(comments, on_delete=models.CASCADE)

class contact(models.Model):
    cont_person_name = models.CharField(max_length=50)
    cont_person_email = models.EmailField(max_length=150)
    cont_person_subject = models.CharField(max_length=50)
    cont_person_message = models.TextField(max_length=500)
