import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobs.settings')
django.setup()


from testapp.models import *
from faker import *
from random import *
fake=Faker()

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','team lead','software engg'))
        feligibility=fake.random_elements(elements=('BE','Btech','BCA','ME'))
        faddress=fake.address()
        femail=fake.email()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail)


populate(10)

def populate1(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','team lead','software engg'))
        feligibility=fake.random_elements(elements=('BE','Btech','BCA','ME'))
        faddress=fake.address()
        femail=fake.email()
        mumbaijobs_record=mumbaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail)


populate1(10)

def populate3(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','team lead','software engg'))
        feligibility=fake.random_elements(elements=('BE','Btech','BCA','ME'))
        faddress=fake.address()
        femail=fake.email()
        punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail)

populate3(10)
