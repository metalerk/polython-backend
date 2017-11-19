from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from stores.models import Store
from users.models import User
from sales.models import Sale
from uuid import uuid4
from utils.utils import get_products_data

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
            sale.set_approved()
        else:
            sale.set_refused()

        sale.save()

        sale.send_email_notification(
            subject="Your order in Polython App",
            message=f"""
Hi {sale.buyer.username}!
\n
The order in {sale.store.name.capitalize()} with ID {sale.pk} was {sale.status.lower()}.
\n
Products: {[product for product in sale.products]}
\n
Amount: ${sale.amount} MXN
\n\n
Sincerely,
\n
Polython App Team.
""",
            recipients=[sale.buyer.email, sale.store.owner.email]
        )

        return JsonResponse({
            'msg': 'ok'
        })
        
    def dispatch(self, *args, **kwargs):
        return super(UpdateSale, self).dispatch(*args, **kwargs)


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
        store = None
        
        try:
            store = Store.objects.get(pk=store_id)
        except:
            return JsonResponse({
                'msg': 'Store does not exist.'
            })

        total, cleaned_products = get_products_data(client_products=products, store_products=store.products)

        print(f"Total: {total}\nProducts: {cleaned_products}")

        sale = Sale(amount=total, products=cleaned_products, buyer=buyer, store=store)
        sale.save()
        return JsonResponse({
            'id': sale.pk.__str__()
        })

    def dispatch(self, *args, **kwargs):
        return super(CreateSale, self).dispatch(*args, **kwargs)