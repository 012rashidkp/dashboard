from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
	#path('post/',views.post,name="upload")

]