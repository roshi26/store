from django.shortcuts import render
from promotions.models import Promotions
from promotions.forms import PromotionsForm
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.

class PromotionView(CreateView):

	template_name='promotions/promotions_form.html'
	form_class=PromotionsForm


	def post(self,request):
		
		if request.method=="POST":
			form=PromotionsForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/promotions/list')
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
