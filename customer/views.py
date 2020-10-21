from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics,permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from productapp.models import Product
from customer.models import Cart, Customers, CartItem
from customer.serializers import ProductSerializer, UserSerializer, RegisterSerializer, ChangePasswordSerializer, CartSerializer, CartItemSerializer, CustomerSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.models import User
from decimal import Decimal
from customer.tasks import send_email_task
import stripe
# Create your views here.

stripe.api_key = "sk_test_51HdsLZKTfVLaT0bRnB15wd0E5BdNUvzbQuvnQPbZGTPfF6TtpXj9v3rdflsUJ8XCsPdQIvLkBX8xtoIXGmQIXUhe0055vq7sJj"

class CustomerListView(generics.ListAPIView):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer

	
	filter_backends=[filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields=['name','price']
	search_fields=['coupon']
	ordering_fields=['price','brand']
	

class RegisterAPI(generics.GenericAPIView): 
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created=Token.objects.get_or_create(user=user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,

     })


class CustomerAPI(generics.GenericAPIView):
    serializer_class=CustomerSerializer
    permission_classes = ( IsAuthenticated,)


    def get_queryset(self,request):
        u=User.objects.get(username=request.user)
        return u


    def post(self,request):
        
        try:
            location=request.data
            print(location['location'])
            Customers.objects.get(location=location['location'])
        except Customers.DoesNotExist:

        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.get_queryset(request))

            stripe_customer=stripe.Customer.create(email=request.user.email, description="My First Test Customer (created for API docs)",)

            stripe.Customer.create_source("cus_IEN4tSHEAoe1ZH",source="tok_mastercard",)

            stripe.Charge.create(
                    amount=2000,currency="inr",source="tok_mastercard",description="My First Test Charge (created for API docs)",)
            send_email_task.delay()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



       


class LoginAPI(TokenObtainPairView): 
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



class ChangePasswordView(generics.UpdateAPIView): 
   
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = ( IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
        
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartView(APIView):
    
    serializer_class=CartSerializer
    model=Cart
    permission_classes = ( IsAuthenticated,)

   

    def get_queryset(self,request):
        c= Customers.objects.get(user=self.request.user)
        return c


    def post(self, request,format=None):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=self.get_queryset(request))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartItemView(APIView):
    serializer_class=CartItemSerializer
    model=CartItem
    permission_classes=(IsAuthenticated,)

    def get_queryset(self,request):
        customer=CartView.get_queryset(self,request)
        ca=Cart.objects.get(customer=customer)
        return ca



    def post(self,request,format=None):
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=self.get_queryset(request))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartItemUpdateView(APIView):
    serializer_class=CartItemSerializer
    model=CartItem


   
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            raise Http404



    def put(self, request, pk=None):
        customer=CartView.get_queryset(self,request)
        cart_item=CartItem.objects.filter(customers=customer)
        total_price=Decimal(0.0)
        for x in cart_item:
            total_price +=  (x.product.price  * x.quantity)
        cart=CartItem.objects.filter(customers=customer).update(total_price=total_price)        

        instance=self.get_object(pk)
        serializer = CartItemSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save(total_price=total_price)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):  #this is to be done
#        pro=request.data
 #       product=Product.objects.get(name=pro)
  #      cart_item=CartItem.objects.filter(product=product).delete()
        instance=self.get_object(pk)
        #instance.delete()

        serializer=CartItemSerializer(instance)
        return Response(serializer.data) 
        return Response(status=status.HTTP_204_NO_CONTENT)
      


