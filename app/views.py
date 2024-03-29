from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

class SignUpView(CreateView):
	template_name='signup.html'
	form_class=UserCreationForm
	def get_success_url(self):
		return redirect('signup.html')


def validate_username(request):
	username=request.GET.get('username',None)
	data ={
	    'is_taken' : User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(data)
