from django import forms
from .models import CareerMail, Contact

class ContactForm(forms.ModelForm):

    class Meta: 
        model = Contact
        fields = '__all__'
        widgets = {
           'full_name' : forms.TextInput(attrs={'class':'form-control',  'required':'required',}),
            'position' : forms.TextInput(attrs={'class':'form-control',  'required':'required',}),
            'office' : forms.TextInput(attrs={'class':'form-control',  'required':'required',}),
            'salary' : forms.TextInput(attrs={'class':'form-control',  'required':'required',}),
           }
        # label = {
		# 'full_name':'Full name'
	    # }
    


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
    
    
   
    

   


    
    
    
   

    


    

  
   