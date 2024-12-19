# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresstype(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    address_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'addresstype'


class Pagedata(models.Model):
    page_data_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=150, blank=True, null=True)
    page_title = models.CharField(max_length=150, blank=True, null=True)
    page_description = models.TextField(blank=True, null=True)
    page_picture = models.CharField(max_length=250, blank=True, null=True)
    page_menu = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagedata'


class Phonetype(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    phone_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'phonetype'


class Useraddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    web_user = models.ForeignKey('Webuser', models.DO_NOTHING)
    street_1 = models.CharField(max_length=50, blank=True, null=True)
    street_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    address_type = models.ForeignKey(Addresstype, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'useraddress'


class Userinfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    web_user = models.ForeignKey('Webuser', models.DO_NOTHING)
    profile_bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.CharField(max_length=150, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Userphone(models.Model):
    user_phone_id = models.AutoField(primary_key=True)
    phone_type = models.ForeignKey(Phonetype, models.DO_NOTHING)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    web_user = models.ForeignKey('Webuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userphone'


class Webuser(models.Model):
    web_user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    password = models.CharField(max_length=40)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webuser'
