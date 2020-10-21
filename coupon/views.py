from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import  UpdateView, DeleteView, CreateView
from coupon.models import  Coupon
from coupon.forms import CouponForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy	


# Create your views here.
class Coupon_view(CreateView):
	
	template_name='coupon/coupon_form.html'
	form_class=CouponForm
	

	def post(self,request):
		
		if request.method=="POST":
			form=CouponForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/list')
		else:
			form=CouponForm()
		return render(request,'coupon/coupon_form.html',{'form':form})

class Coupon_list(ListView):
	model=Coupon
	template_name='coupon/coupon_list.html'
	fields=['expiry_date', 'coupon_number', 'issue_by','issue_to','created_by','recieve_by','product']
	context_object_name= 'coupons'



class Coupon_detail(DetailView):
	model=Coupon
	template_name='coupon/coupon_detail.html'
	context_object_name='coup'



class Coupon_update(UpdateView):
	model=Coupon
	fields=['expiry_date','coupon_number','issue_by','issue_to','created_by','recieve_by','product']
	template_name='coupon/coupon_update.html'
	success_url=reverse_lazy('Coupon_list')


class Coupon_delete(DeleteView):
	model=Coupon
	template_name='coupon/coupon_confirm_delete.html'
	success_url=reverse_lazy('Coupon_list')
