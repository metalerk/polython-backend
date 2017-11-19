from django.views import View
from django.http import JsonResponse
from django.core import serializers
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import login, authenticate, logout

from stores.models import Store

import json


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class StoreDetail(View):
    def get(self, request, pk, *args, **kwargs):        

        store = None
        try:
            store = Store.objects.get(pk=pk.__str__())
        except Exception as e:
            pass

        if store is not None:
            return JsonResponse({
                'id': store.pk.__str__(),
                'name': store.name,
                'products': store.products
            })
        else:
            return JsonResponse({
                'error': 'Store not exist.'
            })

    def dispatch(self, *args, **kwargs):
        return super(StoreDetail, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class CreateStore(View):
    
    def post(self, request, *args, **kwargs):

        name = self.request.POST['name']
        products = self.request.POST['products']
        owner = self.request.user
        
        try:
            Store.objects.get(name=name)
            return JsonResponse({
                'msg': 'Name taken.'
            })

        except:
            pass
        
        try:
            json.loads(product)
            return JsonResponse({
                'msg': 'json malformed.'
            })

        except:
            pass

        store = Store(name=name, products=products, owner=owner)
        store.save()
        return JsonResponse({
            'id': store.pk.__str__()
        })

    def dispatch(self, *args, **kwargs):
        return super(CreateStore, self).dispatch(*args, **kwargs)