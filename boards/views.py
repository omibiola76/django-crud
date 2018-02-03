from django.shortcuts import render
import os
import sys
import imp
import importlib
from django.views.generic import TemplateView
from boards.models import Client
# from utils import get_all_apps_regex, get_non_django_apps_regex, \
#     get_app_name_regex_from_app_urls, get_extra_urls_from_root_urls

class Home(TemplateView):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class AddNewCli(TemplateView):
	template_name = 'addnewcli.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		phone = request.POST['phone']
		email = request.POST['email']

		new_client = Client(fname=first_name, lname=last_name)

		new_client.save()

		print ("Client saved successfully!")
		

		return render(request, self.template_name)

class Tables(TemplateView):
	template_name = 'tables.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class WhiteBoard(TemplateView):
	template_name = 'whiteboard.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
