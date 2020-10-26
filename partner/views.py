from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from partner.forms import PartnerForm
from django.contrib.auth.models import Permission


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
            return HttpResponseRedirect('/partner/login')
        else:
            form=PartnerForm()
            my_dict={'form':form}
        return render(request,'partner/partner.html', {'form':partner_form})




class ProfileView(View):
    login_url='/login/'
    template_name='partner/profile.html'
    redirect_field_name='/partner/login/'
    
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
            return HttpResponseRedirect('/partner/login/profile')
        else:
            state="inactive"
        return render(request,'partner/login.html',{'state':state})



class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return render(request,'partner/login.html')












