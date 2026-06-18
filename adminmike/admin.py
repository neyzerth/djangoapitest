from django.contrib import admin

from adminmike.models import School, Student, Teacher

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
