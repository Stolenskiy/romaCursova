# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Labka(models.Model):
    nuber = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=50, blank=True, null=True)
    brief_description = models.CharField(max_length=500, blank=True, null=True)
    max_bal = models.FloatField(blank=True, null=True)
    predmet_teacher = models.ForeignKey('PredmetTeacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labka'


class Para(models.Model):
    predmet_teacher = models.ForeignKey('PredmetTeacher', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'para'


class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class PredmetList(models.Model):
    predet_name = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predmet_list'


class PredmetTeacher(models.Model):
    predmet = models.ForeignKey(PredmetList, models.DO_NOTHING, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predmet_teacher'


class Student(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    date_of_entry = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentsLab(models.Model):
    labka = models.ForeignKey(Labka, models.DO_NOTHING, blank=True, null=True)
    bal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students_lab'


class Teacher(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    naukova_stepin = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'
