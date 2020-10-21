from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from partner.forms import PartnerForm
from employee.models import Employee
from productapp.models import Product
from coupon.models import Coupon
from promotions.models import Promotions
from employee.forms import EmployeeForm
from productapp.forms import ProductForm
from coupon.forms import CouponForm
from promotions.forms import PromotionsForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import PermissionRequiredMixin

class PartnerView(FormView):

    template_name='partner/partner.html'
    form_class=PartnerForm

    def post(self,request):
        if request.method=="POST":
            partner_form=PartnerForm(request.POST)
            if partner_form.is_valid():
                partner=partner_form.save()
                partner.set_password(partner.password)
                partner.is_staff = True
                permission=Permission.objects.get(name='Can view coupon' )#to give index for employee
                partner.user_permissions.add(permission)
                partner.save()
                return HttpResponseRedirect('/login')
        else:
            form=PartnerForm()
            my_dict={'form':form}
        return render(request,'partner/partner.html', {'form':partner_form})



class ProfileView(View):
    login_url='/login/'
    template_name='partner/profile.html'
    redirect_field_name='/login/'
    def get(self,request):
        return render(request,'partner/profile.html')

    def post(self,request):
        return render(request,'partner/profile.html')

    

class LoginView(View):
   
    def get(self, request):
        return render(request,'partner/login.html')
    
    def post(self,request):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/login/profile')
        else:
            state="inactive"
        return render(request,'partner/login.html',{'state':state})


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return render(request,'partner/login.html')



class EmployeeView(View):
   # model=Employee
    template_name='employee/employee_form.html'
    form_class=EmployeeForm

    def get(self,request):
        form=EmployeeForm
        context={'form':form}
        return render(request,'employee/employee_form.html',context)


    
    def post(self,request):
        
        if request.method=="POST":
            form=EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/elist')
        else:
            form=ProductForm()
        return render(request,'employee/employee_form.html',{'form':form})



class EmployeeList(ListView):
    model=Employee
    template_name='employee/employee_list.html'
    context_object_name='employees'

    def get_queryset(self):
         return Employee.objects.filter(created_by=self.request.user)



class EmployeeUpdate(UpdateView):
    model=Employee
    template_name='employee/employee_update.html'
    fields=['first_name','last_name','id_number','phone_number','job_title','department','email','location','start_date','end_date']
    success_url=reverse_lazy('emp_list')



class EmployeeDetail(DetailView):
    model=Employee
    template_name='employee/employee_detail.html'
    context_object_name='emp'



class EmployeeDelete(DeleteView):
    model=Employee
    template_name='employee/employee_confirm_delete.html'
    success_url=reverse_lazy('emp_list')



class ProductView(View):
    
    template_name='productapp/product_form.html'
    form_class=ProductForm

    def get(self,request):
        form=ProductForm
        {'form':form}
        return render(request,'productapp/product_form.html',{'form':form})


    
    def post(self,request):
        
        if request.method=="POST":
            form=ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/prolist')
        else:
            form=ProductForm()
        return render(request,'productapp/product_form.html',{'form':form})



class ProductList(ListView):
    model=Product
    template_name='product/product_list.html'
    context_object_name='object_list'


    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)


class ProductUpdate(UpdateView):
    model=Product
    fields=['name','created_at', 'price','quality', 'issue_by', 'issue_to','brand','coupon','issue_to','discount']
    template_name='productapp/product_form.html'
    success_url=reverse_lazy('product_list')


class ProductDetail(DetailView):
    model=Product
    template_name='productapp/product_detail.html'
    context_object_name="ob"



class ProductDelete(DeleteView):
    model=Product
    template_name='productapp/product_delete.html'
    success_url=reverse_lazy('pro_list')


class CouponView(View):
    template_name='coupon/coupon_form.html'
    form_class=CouponForm


    def get(self,request):
        form=CouponForm
        return render(request,'coupon/coupon_form.html',{'form':form})
    
    def post(self,request):
        
        if request.method=="POST":
            form=CouponForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/coulist')
        else:
            form=CouponForm()
        return render(request,'coupon/coupon_form.html',{'form':form})



class CouponList(ListView):
    model=Coupon
    template_name='coupon/coupon_list.html'
    fields=['expiry_date', 'coupon_number', 'issue_by','issue_to','created_by','recieve_by','product']
    context_object_name= 'coupons'


    def get_queryset(self):
        return Coupon.objects.filter(created_by=self.request.user)



class CouponDetail(DetailView):
    model=Coupon
    template_name='coupon/coupon_detail.html'
    context_object_name='coup'


class CouponUpdate(UpdateView):
    model=Coupon
    fields=['expiry_date','coupon_number','issue_by','issue_to','created_by','recieve_by','product']
    template_name='coupon/coupon_update.html'
    success_url=reverse_lazy('Coupon_list')



class CouponDelete(DeleteView):
    model=Coupon
    template_name='coupon/coupon_confirm_delete.html'
    success_url=reverse_lazy('Coupon_list')


class PromotionView(View):
    
    template_name='promotions/promotions_form.html'
    form_class=PromotionsForm
    permission_required=('promotions.view promotions')


    def get(self,request):
        form=PromotionsForm
        return render(request,'promotions/promotions_form.html',{'form':form})
    def post(self,request):
        
        if request.method=="POST":
            form=PromotionsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/promlist')
        else:
            form=PromotionsForm()
        return render(request,'promotions/promotions_form.html',{'form':form})



class PromotionList(ListView):
    model=Promotions
    template_name='promotions/promotions_list.html'
    fields=['day','created_at','modified_at','created_by','modified_by']
    context_object_name='promotions'


    def get_queryset(self):
        return Promotions.objects.filter(created_by=self.request.user)

        

class PromotionDetail(DetailView):
    model=Promotions
    template_name='promotions/promotions_detail.html'
    context_object_name='pro'


class PromotionUpdate(UpdateView):
    model=Promotions
    template_name='promotions/promotions_update.html'
    fields=['day','created_by','modified_by']
    success_url=reverse_lazy('promotions_list')


class PromotionDelete(DeleteView):
    model=Promotions
    template_name='promotions/promotions_delete.html'
    success_url=reverse_lazy('promotions_list')
