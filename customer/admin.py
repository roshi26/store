from django.contrib import admin
from customer.models import Customers, Cart, CartItem
# Register your models here
class CustomerAdmin(admin.ModelAdmin):
	list_display=['location','id']
admin.site.register(Customers, CustomerAdmin)


admin.site.register(Cart)


admin.site.register(CartItem)