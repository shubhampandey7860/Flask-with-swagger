"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import YourModelViewSet
from app.views import your_model_list, your_model_detail,YourModelAPIView , file_upload,success_view

router = DefaultRouter()
router.register(r'yourmodels', YourModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #("",include(router.urls)),
    # path('yourmodels/', your_model_list),
    # path('yourmodels/<int:pk>/', your_model_detail),
    path('yourmodels', YourModelAPIView.as_view()),  
    path('yourmodels/<int:pk>/', YourModelAPIView.as_view()),  
    path('', file_upload, name='file_upload'),
    path('success/', success_view, name='success_url'), 
]
