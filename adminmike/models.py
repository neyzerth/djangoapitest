from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hired_at = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=100)
    semesters = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

