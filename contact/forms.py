from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget = forms.TextInput(attrs={'class':'form-control','id':'name' ,'placeholder':'Ingresa tu nombre...'}), min_length=3, max_length = 100)
    email = forms.EmailField(label="Email", required=True, widget = forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Escribe tu correo...'}), min_length=3, max_length = 100)
    phone = PhoneNumberField(label="Phone", required=True, widget = forms.NumberInput(attrs={'class':'form-control','id':'phone','type':'number','placeholder':'(951) 456-7890'}), min_length=3, max_length = 15)
    content = forms.CharField(label="Contenido", required=True, widget = forms.Textarea(attrs={'class':'form-control', 'rows': '5', 'id':'message','style':'height: 10rem','placeholder':'Escribre tu mensaje'}), min_length=3, max_length = 100)