from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from home.models import Student,Library,Book,Sectionn,Teacher

#from .models import Student
#from account.models import AccInfo
#admin.site.register(Student)
#admin.site.register(Library)
#admin.site.register(Book)
#admin.site.register(Sectionn)
#admin.site.register(Teacher)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','department')
    list_filter=('student_name','department')
    fields=('student_name','department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Sectionn)
class SectionnAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass
