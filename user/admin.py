from django.contrib import admin

from .models import Courses, Mentor, Student, Language

admin.site.register(Courses)
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Language)
