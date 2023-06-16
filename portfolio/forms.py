from django import forms

class Contact (forms.Form):
    title = forms.CharField(max_length= 200, label='Nombre')
    description = forms.CharField(label= "Mensaje", widget=forms.Textarea)


