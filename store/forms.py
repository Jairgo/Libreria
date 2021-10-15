from django import forms
from django.forms import fields, widgets
from .models import Store
# from phonenumber_field.formfields import PhoneNumberField

class createBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Store
        fields = ['title', 'description', 'book']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','id':'name' ,'placeholder':'Ingresa tu nombre...'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'rows': '5', 'id':'message','style':'height: 10rem','placeholder':'Escribre tu mensaje'}),
            'book': forms.FileInput(attrs={'class':'form-control-file','id':'file' ,}),
        }

class updateBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Store
        fields = ['title', 'description', 'book']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','id':'name' ,'placeholder':'Ingresa tu nombre...'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'rows': '5', 'id':'message','style':'height: 10rem','placeholder':'Escribre tu mensaje'}),
            'book': forms.FileInput(attrs={'class':'form-control','id':'file' ,}),
        }
