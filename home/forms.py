from django import forms
from .models import Student
class studentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
                'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'student'}),
                 'department':forms.Select(attrs={'class':'custom-select'})
        }

class studentsearchform(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max-length':'30','placeholder':'search'}))

class studentcreateform(forms.Form):
    student_name=forms.CharField(label="",widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'student.name'}))
    dept=(('ise','information science'),('mh','mech'),('cv','cvil'))
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))