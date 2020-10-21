from rest_framework import serializers
from productapp.models import Product
from django.contrib.auth.models import User
from customer.models import Cart, CartItem, Customers

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields=['name','created_at','price','quality','issue_by','issue_to','last_updated','brand','quantity','coupon','created_by']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user =User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user




class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        


        model=Customers
        fields=['user','phone_number','location']
        



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=('date_created','total_price')
    

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['quantity','product','customers','cart','total_price']
   

