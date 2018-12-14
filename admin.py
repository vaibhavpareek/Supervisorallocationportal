from django.contrib import admin
from .models import Student,Supervisor,Profile, Data

admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Profile)
admin.site.register(Data)
