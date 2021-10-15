from django import forms
# from phonenumber_field.formfields import PhoneNumberField

class createBookForm(forms.Form):
    title = forms.CharField(label="Nombre", required=True, widget = forms.TextInput(attrs={'class':'form-control','id':'name' ,'placeholder':'Ingresa tu nombre...'}), min_length=3, max_length = 100)
    content = forms.CharField(label="Contenido", required=True, widget = forms.Textarea(attrs={'class':'form-control', 'rows': '5', 'id':'message','style':'height: 10rem','placeholder':'Escribre tu mensaje'}), min_length=3, max_length = 100)
    file = forms.FileField(label="Archivo", required=True, widget= forms.FileInput(attrs={'class':'form-control','id':'file' ,}))
