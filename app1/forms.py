from app1.models import Student
from django import forms

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['stuname', 'stuemail', 'stuphone']
        widgets = {
            'stuname':forms.TextInput(attrs={'class':'form-control'}),
            'stuemail':forms.EmailInput(attrs={'class':'form-control'}),
            'stuphone':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'stuname':'Name',
            'stuemail':'Email',
            'stuphone':'Phone',
        }