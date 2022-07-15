"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from productapp.views import ProductInput,ProductInsert,DisplayView,DeleteInputView,UpdateView,UpdateInputView,HomeView,DeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('productapp/', HomeView.as_view()),
    path('productapp/ProductInput/', ProductInput.as_view()),
    path('productapp/insert/',ProductInsert.as_view()),
    path('productapp/display/',DisplayView.as_view()),
    path('productapp/deleteinput/',DeleteInputView.as_view()),
    path('productapp/deleteinput/delete',DeleteView.as_view()),
    path('productapp/updateinput/',UpdateInputView.as_view()),
    path('productapp/Updateinput/update/',UpdateView.as_view())
]
