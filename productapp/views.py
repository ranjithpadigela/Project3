from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class ProductInput(View):
    def get(self,request):
        return render(request,'Productinput.html')

class ProductInsert(View):
    def get(self,request):
        p_id = request.GET['t1']
        p_name = request.GET['t2']
        p_cost = request.GET['t3']
        p_mfdt = request.GET['t4']
        p_expdt = request.GET['t5']
        p1 = Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res = HttpResponse("Product are created Successfully")
        return res
class DisplayView(View):
    def get(self,request):
        qs = Product.objects.all()
        con_dic = {"records":qs}
        return render(request,'display.html',con_dic)

class DeleteInputView(View):
    def get(self,request):
        return render(request,'deleteinput.html')

class DeleteView(View):
    def get(self,request):
        P_id = int(request.GET['t1'])
        prod = Product.objects.first(pid=P_id)
        prod.delete()
        res = HttpResponse("Product deleted successfully")
        return res
class UpdateInputView(View):
    def get(self,request):
        return render(request,'updateinput.html')
class UpdateView(View):
    def post(self,request):
        P_id = int(request.POST['t1'])
        P_name = (request.POST['t2'])
        P_cost = float((request.POST['t3']))
        P_mfdt = (request.POST['t4'])
        P_expdt = (request.POST['t5'])
        prod = Product.objects.get(pid=P_id)
        prod.pname = P_name
        prod.pcost = P_cost
        prod.pmfdt = P_mfdt
        prod.pexpdt = P_expdt
        prod.save()
        res = HttpResponse("The product updated successfully")
        return res