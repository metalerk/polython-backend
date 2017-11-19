from stores.models import Store
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.urls import resolve

from stores.serializers import StoreSerializer
 
 
class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
 
    def get_queryset(self):
    	temp1, args, kwargs = resolve(self.request.path)
    	print(temp1, args, kwargs)
    	return Store.objects.all().filter(pk=kwargs['pk'])