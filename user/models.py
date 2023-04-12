from datetime import timedelta
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.name == self.name.lower():
            self.name = self.name.title()
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number.startswith('0') and len(self.phone_number) == 10:
            self.phone_number = '+996' + self.phone_number[1:]
        elif self.phone_number.startswith('0') and len(self.phone_number) == 13:
            self.phone_number = '+' + self.phone_number[1:]
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=20, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=20, choices=(
        ('windows', 'Windows'),
        ('macos', 'MacOS'),
        ('linux', 'Linux'),
    ))


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=60, null=True, blank=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, through='Courses')


class Courses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()

    def get_end_date(self):
        completion_date = self.date_started + timedelta(days=30 * self.language.month_to_learn)
