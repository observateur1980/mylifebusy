from django.shortcuts import render
from django.views.generic.base import TemplateView,View
import random
from home.models import Category,SubCategory
from . forms import ContactForm, CareerMailForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from pip._vendor import requests
from django.utils import timezone
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
	template_name = 'home/home.html'
	
	
class Table(TemplateView):
	template_name = 'home/table.html'

class Sugar(View):
	template_name = 'home/sugar.html'

	def get(self, request, *args, **kwargs):
		cat_id = kwargs['cat_id']
		
		qs_subcats = SubCategory.objects.all().values('title','price','categories__title').filter(categories=cat_id)
		# if ther is no any sub cat we must avoid 
		# to send ampty dic to the templa cause it gives us error
		if(qs_subcats):
			cat = qs_subcats[0]['categories__title']
			context = {
				'menu':			"servicemenu",	
				'qs_subcats': 	qs_subcats,
				'cat': cat
			}
		else :
			context = {
				'menu':			"servicemenu",
				'cat': "There is no any sub cat"
			}

		
		
		return render(request, self.template_name, context)	


		

class Service(TemplateView):
	template_name = 'home/service.html'
	
	def get(self, request, *args, **kwargs):
		qs = SubCategory.objects.all().values('title','price','categories__id','categories__title','icon__icon_tag').filter(categories__active=True).order_by('categories__id')
		context = {
			'menu':			"servicemenu",	
			'qs': 	qs,
			
		}
		return render(request, self.template_name, context)	


class Contact(FormView):
	template_name = 'home/contact.html'
	form_class = ContactForm
	success_url = 'success_sent'


	def get_context_data(self, *args, **kwargs):
		context = super(Contact, self).get_context_data(*args, **kwargs)
		context["menu"] = 'contactmenu'
		return context
	
	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
		verify = result["success"]
		''' End reCAPTCHA validation '''
		
		if form.is_valid():
			if verify:
				return self.form_valid(form, **kwargs)
			else: 
				messages.warning(request, 'Please correct the reCAPTCHA error below.')
				return self.form_invalid(form, **kwargs)
		else:
			
			return self.form_invalid(form, **kwargs)
	
	
	
	def form_valid(self, form):
		name = form.cleaned_data['name']
		phone = form.cleaned_data['phone']
		email = form.cleaned_data['email']
		subject = form.cleaned_data['subject']
		message =form.cleaned_data['message']
		message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + message
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['info@mylifebusy.com',]
		send_mail( subject, message, email_from, recipient_list )
		return super(Contact, self).form_valid(form)

	def form_invalid(self, form, **kwargs):
		context = self.get_context_data(**kwargs)
		context['form'] = form
		return self.render_to_response(context)

		


class ComingSoon(TemplateView):
	template_name = 'home/comingsoon.html'
	
	def get_context_data(self, **kwargs):
		context = super(ComingSoon, self).get_context_data(**kwargs)
		context['menu'] = "comingsoonmenu"
		return context
	

class PrivacyPolicy(TemplateView):
	template_name = 'home/privacy_policy.html'

class Terms(TemplateView):
	template_name = 'home/terms.html'

class SuccessSent(TemplateView):
	template_name = 'home/success_sent.html'

class Career(TemplateView):
	template_name = 'home/career.html'
	form_class = CareerMailForm
	
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'menu': 'careermenu','form':form,})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
		verify = result["success"]
		''' End reCAPTCHA validation '''
		
		if form.is_valid():
			print('form is valid')
			if verify:
				post = form.save(commit=False)
				post.published_date = timezone.now()
				post.save()

				full_name = form.cleaned_data['full_name']
				phone = form.cleaned_data['phone']
				email = form.cleaned_data['email']
				looking_for = form.cleaned_data['looking_for']
				document = request.FILES.get('document')
				reference =form.cleaned_data['reference']
				message = 'Name: ' + full_name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + looking_for + '\n' + reference
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['info@mylifebusy.com',]
				try:
					print("try")
					mail = EmailMessage(
						'Letter name comes here',
						message,
						email_from,
						recipient_list,
					)
					mail.attach_file('media/documents/'+str(document))
					mail.send()
					return HttpResponseRedirect(reverse('home:success_sent'))
					
				except:
					messages.warning(request, 'Corrupted file or too big file size.')
					return render(request, self.template_name, {'form': form,})
			
			else: 
				messages.warning(request, 'Please correct the reCAPTCHA error below.')
				return render(request, self.template_name, {'form': form,})
			
		print('form is invalid')
		messages.warning(request, 'Posted form is invalid.')
		return render(request, self.template_name, {'form': form})


class MyTest(View):
	template_name = 'home/mytest.html'
	form_class = CareerMailForm
	success_url = 'success_sent'

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(MyTest, self).get_context_data(*args, **kwargs)	
	# 	context["menu"] = 'careermenu'
	# 	return context

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'menu': 'careermenu','form':form,})

	def post(self, request, *args, **kwargs):
		
		# form_class = self.get_form_class()
		# form = self.get_form(form_class)
		form = self.form_class(request.POST, request.FILES)
		
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
		verify = result["success"]
		''' End reCAPTCHA validation '''
		
		if form.is_valid():
			print('form is valid')
			if verify:
				post = form.save(commit=False)
				post.published_date = timezone.now()
				post.save()

				full_name = form.cleaned_data['full_name']
				phone = form.cleaned_data['phone']
				email = form.cleaned_data['email']
				looking_for = form.cleaned_data['looking_for']
				document = request.FILES.get('document')
				reference =form.cleaned_data['reference']
				message = 'Name: ' + full_name + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + email + '\n' + looking_for + '\n' + reference
				email_from = settings.EMAIL_HOST_USER
				recipient_list = ['info@mylifebusy.com',]
				try:
					print("try")
					mail = EmailMessage(
						'Letter name comes here',
						message,
						email_from,
						recipient_list,
					)
					mail.attach_file('media/documents/'+str(document))
					mail.send()
					return HttpResponseRedirect(reverse('home:success_sent'))
					
				except:
					messages.warning(request, 'Corrupted file or too big file size.')
					return render(request, self.template_name, {'form': form,})
			
			else: 
				messages.warning(request, 'Please correct the reCAPTCHA error below.')
				return render(request, self.template_name, {'form': form,})
			
		print('form is invalid')
		messages.warning(request, 'Posted form is invalid.')
		return render(request, self.template_name, {'form': form})

			
			
			

			

			

			

			
		
		

			
			

				
			

	
	


		
		
	

	
