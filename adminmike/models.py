from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Course(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=20, unique=True)
#     description = models.TextField(blank=True)
#     students = models.ManyToManyField(Student, related_name='courses', blank=True)
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return f"{self.name} ({self.code})"

