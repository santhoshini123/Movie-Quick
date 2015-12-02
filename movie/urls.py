from django.conf.urls import url
from . import views
urlpatterns = [
<<<<<<< HEAD
	url(r'^$',views.register, name = 'register'),
	# url(r'^$',views.index, name='index'),
	url(r'^home/$',views.validate),
	url(r'validatelogin/$',views.validatelogin, name='validatelogin'),
	url(r'validate/$',views.validate, name='validate'),
	# url(r'validatelogin123/$',views.validatelogin123, name='validatelogin123'),
=======
	url(r'^register$/',views.register, name = 'register'),
	url(r'^$',views.index, name='index'),
	url(r'^home$/',views.validate),
>>>>>>> ce9d6cf5dc1a52392c88f3d04c3dc7bf193ba42c
]