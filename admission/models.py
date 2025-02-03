from django.db import models

class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 500, null=True)
    code = models.CharField(max_length = 15, null=True)
    type = models.CharField(max_length = 15, null=True)
    rank = models.IntegerField(null = True)
    web_site = models.CharField(max_length = 500, null=True)
    image = models.CharField(max_length = 500, null=True) #600x400
    programs = models.CharField(max_length = 500, null=True)
    location = models.CharField(max_length = 500, null=True)
    success_number = models.CharField(max_length = 500, null=True)
    # alive = models.BooleanField(null=True)
    attribute_1 = models.CharField(max_length = 500, null=True)
    attribute_2 = models.CharField(max_length = 500, null=True)
    attribute_3 = models.CharField(max_length = 500, null=True)
    created_by = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by = models.IntegerField(null = True)
    modified_date = models.DateTimeField(null = True)

class Client_Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 500, null=True)
    email = models.CharField(max_length = 100, null=True)
    phone = models.CharField(max_length = 50, null=True)
    whatsapp = models.CharField(max_length = 50, null=True)
    program = models.IntegerField(null = True)
    subject = models.CharField(max_length = 15, null=True)
    qualification = models.CharField(max_length = 5000, null=True)
    attribute_1 = models.CharField(max_length = 500, null=True)
    attribute_2 = models.CharField(max_length = 500, null=True)
    attribute_3 = models.CharField(max_length = 500, null=True)
    created_by = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by = models.IntegerField(null = True)
    modified_date = models.DateTimeField(null = True)

class Client_Query(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 500, null=True)
    email = models.CharField(max_length = 100, null=True)
    subject = models.CharField(max_length = 5000, null=True)
    message = models.CharField(max_length = 5000, null=True)
    attribute_1 = models.CharField(max_length = 500, null=True)
    attribute_2 = models.CharField(max_length = 500, null=True)
    attribute_3 = models.CharField(max_length = 500, null=True)
    created_by = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by = models.IntegerField(null = True)
    modified_date = models.DateTimeField(null = True)