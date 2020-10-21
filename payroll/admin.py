from django.contrib import admin
from payroll.models import Payroll
from django import forms



class PayrollAdmin(admin.ModelAdmin):
	list_display=('employee','salary','gross_pay','net_pay','month','year','created_at','modified_at','tax')
	list_filter=("employee",)
	search_fields=("month",)

admin.site.register(Payroll,PayrollAdmin)




	


	
