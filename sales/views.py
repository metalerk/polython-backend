from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from stores.models import Store
from users.models import User
from uuid import uuid4

import json


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class UpdateSale(View):

    request_data = None

    def post(self, request, pk, *args, **kwargs):

        self.request_data = json.loads(self.request.body)
        status = self.request_data['status']
        sale = None
        
        try:
            sale = Sale.objects.get(pk=pk.__str__())
        except Exception as e:
            return JsonResponse({
                'error': 'Sale ID not valid.'
            })

        if status == "ACCEPTED":
            sale.status = "ACCEPTED"
        else:
            sale.status = "REFUSED"

        sale.save()

        return JsonResponse({
            'msg': 'ok'
        })
        
    def dispatch(self, *args, **kwargs):
        return super(StoreDetail, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class CreateSale(View):

    request_data = None 
    
    def post(self, request, *args, **kwargs):

        self.request_data = json.loads(self.request.body)

        store_id = self.request_data['store_id']
        amount = self.request_data['total_amount']
        products = self.request_data['products']
        buyer = self.request.user
        
        try:
            Store.objects.get(pk=store_id)
        except:
            return JsonResponse({
                'msg': 'Store does not exist.'
            })
        
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