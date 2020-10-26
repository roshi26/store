from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import  UpdateView, DeleteView, CreateView
from coupon.models import  Coupon
from coupon.forms import CouponForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy	


# Create your views here.
class CouponView(CreateView):
	
	template_name='coupon/coupon_form.html'
	form_class=CouponForm
	

	def post(self,request):
		
		if request.method=="POST":
			form=CouponForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/coupon/list')
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
