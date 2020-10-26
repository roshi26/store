from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from productapp.models import Product
from productapp.forms import ProductForm
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
class ProductView(CreateView):
	template_name='productapp/product_form.html'
	form_class=ProductForm
	

	def post(self,request):
		
		if request.method=="POST":
			form=ProductForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/product/list')
		else:
			form=ProductForm()
		return render(request,'productapp/product_form.html',{'form':form})
		

class ProductListView(ListView):
	model=Product
	template_name='productapp/product_list.html'
	fields=['name','created_at', 'price', 'quality','issue_by', 'issue_to', 'brand', 'quantity', 'coupon', 'discount']
	context_object_name="object_list"
	
	def get_queryset(self):
		return Product.objects.filter(created_by=self.request.user)
	


class ProductDetailView(DetailView):
	model=Product
	template_name='productapp/product_detail.html'
	context_object_name="ob"



class ProductUpdateView(UpdateView):
	model=Product
	fields=['name','created_at', 'price','quality', 'issue_by', 'issue_to','brand','coupon','issue_to','discount']
	template_name='productapp/product_form.html'
	success_url=reverse_lazy('product_list')


	
class ProductDeleteView(DeleteView):
	model=Product
	template_name='productapp/product_delete.html'
	success_url=reverse_lazy('product_list')

	

