from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
	path('changepass/', views.changepass),
	path('printcard/', views.printcard),
	path('printcard2/', views.printcard2),
	path('userlist/', views.userlist),
	path('edituser/', views.edituser),
	path('deluser/', views.deluser),
	path('signin/', views.signin),
	path('logout/', views.logout_form),
	path('uploadtpl/', views.uploadtpl),
	path('printalluser/', views.printalluser),
]

