
#省略了前面的网站url即（http://127.0.0.1:8000/bb/05)为全称



from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name='index'),
	#path('05/',views.blog,name='blog')
	]