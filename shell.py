import datetime
from django.utils import timezone
from user.models import Student, Mentor, Language, Courses
Language.objects.all()
l_1 = Language(name='Python', month_to_learn=6)
l_2 = Language(name='Java Script', month_to_learn=6)
l_3 = Language(name='UX-UI', month_to_learn=2)
l_1.save()
l_2.save()
l_3.save()
s_1 = Student(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898', work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
s_1.save()
s_2 = Student(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888', work_study_place='TV', has_own_notebook=True, preferred_os='mac')
s_2.save()
s_3 = Student(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')
s_3.save()
m_1 = Mentor(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454', main_work=None, experience=datetime.date(year=2010, month=10, day=23))
m_1.save()
m_2 = Mentor(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876', main_work='University of Fort Collins', experience=datetime.date(year=2010, month=9, day=18))
m_2.save()
c_1 = Courses.objects.create(name="Python – 21", language=Language.objects.get(name="Python"), date_started=timezone.datetime(2022, 8, 1), mentor=Mentor.objects.get(name='Halil Nurmuhametov'), student=Student.objects.get(name='Amanov Aman'))
c_2 = Courses.objects.create(name="UXUI design – 43", language=Language.objects.get(name="UX-UI"), date_started=timezone.datetime(2022, 8, 22), mentor=Mentor.objects.get(name='Ilona Maskova'), student=Student.objects.get(name='Phil Spencer'))
c_1.save()
c_2.save()