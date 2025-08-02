from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



class CustomLoginView(LoginView):
	template_name = 'profile/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('posts:main-post-view')


def home_view(request):
	user = request.user
	hello = 'Hello world.!'
	context = {
		'user': user,
		'hello': hello
	}
	return render(request, 'main/home.html', context)
	# return HttpResponse('Hello World.!')