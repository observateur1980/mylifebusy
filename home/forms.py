from django import forms
from .models import CareerMail

class ContactForm(forms.Form):
    name = forms.CharField( max_length=120, widget=forms.TextInput(attrs={'id':'contact-name','name' :'contact-name', 'required':'required'}))
    email = forms.EmailField(max_length=120, widget=forms.EmailInput(attrs={'id':'contact-email','name':'contact-email',  'class':'m-required m-email','required':'required'}))
    phone = forms.CharField( max_length=12, required=False, widget=forms.TextInput(attrs={'id':'contact-phone','name' : 'contact-phone'}))
    subject = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'id':'contact-subject', 'name':'contact-subject'}))
    message = forms.CharField( max_length=2000, widget=forms.Textarea(attrs={'id':'contact-message', 'name':'contact-message', 'required':'required'}))


class CareerMailForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'id':'contact-name','name' :'contact-name', 'required':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'contact-email','name':'contact-email',  'class':'m-required m-email','required':'required'}))
    phone = forms.CharField( required=False, widget=forms.TextInput(attrs={'id':'contact-phone','name' : 'contact-phone'}))
    looking_for = forms.CharField(required=False, widget=forms.TextInput(attrs={'id':'contact-subject', 'name':'contact-subject'}))
    document = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    reference = forms.CharField(widget=forms.Textarea(attrs={'id':'contact-message', 'name':'contact-message', 'required':'required'}))

    class Meta:
        model = CareerMail
        fields = ('full_name','email','phone','looking_for','document', 'reference')
    
    
   
    

   


    
    
    
   

    


    

  
   